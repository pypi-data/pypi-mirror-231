from __future__ import absolute_import, division, print_function, unicode_literals

import os
import shutil
import stat
import subprocess
import sys
import tempfile

import publisher.settings as settings
from publisher.exceptions import ProcedureCreationError, UpdateNoteError
from publisher.git_handling.history import (
    UsingCommit,
    change_branch,
    get_commits_for_phase,
    get_commits_for_procedure,
)
from publisher.git_handling.notes import clear_similar_historical_notes, edit_note
from publisher.git_handling.setup import install_studio_report_tool, node_installed
from publisher.utils import (
    WorkingDirectory,
    call_command_and_print_exception,
    get_command_output,
    get_content_directories,
    get_input,
    get_procedure_code,
    get_user_commit_selection,
    get_yes_no,
)
from publisher.validators import validate_save


def build_channel_list(with_update=True):

    """ Lists all current branches of the repository
    """

    if os.path.exists(settings.CHANNELS_CHECKOUT_DIRECTORY):
        if with_update:
            with WorkingDirectory(settings.CHANNELS_CHECKOUT_DIRECTORY):
                pull_and_merge()

        channels = [
            name
            for name, ext in (
                os.path.splitext(item)
                for item in os.listdir(settings.CHANNELS_CHECKOUT_DIRECTORY)
            )
            if ext == ".yml"
        ]

        return channels
    else:
        raise Exception('You do not have the content-channels repository, please run the setup command.')


def build_procedure_list(with_update=True):

    """ Lists all current branches of the repository
    """

    def is_procedure(p):
        return p not in ["master", "HEAD", "->", "*"] and p.strip() != ""

    if os.path.exists(settings.PROCEDURE_CHECKOUT_DIRECTORY):
        with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
            if with_update:
                print("Getting updates from repository")
                subprocess.run(
                    ["git", "-c", "protocol.version=2", "fetch", "--quiet"], check=True
                )

            print("Getting list of branches")
            output, _ = get_command_output(["git", "branch", "-a"])
            procedures = filter(
                is_procedure, {name.split("/")[-1] for name in output.split()}
            )

            return list(procedures)

    else:
        raise Exception('You do not have the content-production repository, please run the setup command.')


def display_procedures():
    print('\n'.join(build_procedure_list()))


def build_phase_list():
    """ Returns a list of phases for the current module
    """
    procedure_directories = get_content_directories(settings.PROCEDURE_CHECKOUT_DIRECTORY)
    if len(procedure_directories) == 0:
        return []

    phase_folder = os.path.join(settings.PROCEDURE_CHECKOUT_DIRECTORY, procedure_directories[0])
    return get_content_directories(phase_folder)


def get_user_selected_phase():
    phases = sorted(build_phase_list())
    return get_user_commit_selection('\nSelect a phase to display its history (0 to cancel)', phases)


def display_phase_history(phase):
    print("\n".join([str(c) for c in get_commits_for_phase(phase)]))


def revert_phase_commit(phase, commit_id):
    """ Get the phase folders state at a certain commit and copy it into the latest version of the branch, unsaved.
    """
    current_procedure = get_procedure_code()
    temp_phase_dir = tempfile.mkdtemp()
    phase_path = os.path.join(settings.PROCEDURE_CHECKOUT_DIRECTORY, current_procedure, phase)

    with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
        print('Performing checkout of commit {}'.format(commit_id))
        call_command_and_print_exception(['git', 'checkout', '-q', commit_id], 'Could not checkout specified commit.')
        shutil.copytree(phase_path, os.path.join(temp_phase_dir, phase))
        print('Performing checkout of branch {}'.format(current_procedure))
        call_command_and_print_exception(['git', 'checkout', '-q', current_procedure],
                                         'Could not revert to latest commit.')
        shutil.rmtree(phase_path, onerror=remove_readonly)

        shutil.copytree(os.path.join(temp_phase_dir, phase), os.path.join(current_procedure, phase))
        shutil.rmtree(temp_phase_dir, onerror=remove_readonly)


def display_phase_history_and_revert(phase_code):
    if not phase_code:
        sys.exit(0)
    with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
        output, _ = get_command_output(['git', 'status'])
        if 'working tree clean' in output:
            message = "\nEnter the number of the version you want to revert to (0 to cancel):"
            user_input = get_user_commit_selection(message, get_commits_for_phase(phase_code))
            if not user_input:
                sys.exit(0)
            revert_phase_commit(phase_code, user_input.id)
            print(phase_code + " has been reverted to the selected commit.")
        else:
            print('You have unsaved changes, please commit them or perform a tspub reset before reverting to a '
                  'different commit.')


def reset_repo():
    """ Git reset
    """
    with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
        print('Performing git reset')
        call_command_and_print_exception(['git', 'reset', '--hard', '--quiet'], "Could not perform git reset.")
        print('Performing git clean')
        call_command_and_print_exception(['git', 'clean', '-f', '-d', '-q'], "Could not perform git clean.")


def cl_reset_repo():
    """ Git reset with user interaction
    """
    print("Resetting will lose any unsaved changes, are you sure you wish to continue? (y or n):")
    sys.stdout.flush()
    reset_confirmation = get_yes_no()
    if reset_confirmation:
        reset_repo()
    else:
        print("Operation cancelled.")


def remove_readonly(func, path, _):
    """Clear the readonly bit and reattempt the removal
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def _case_match_procedure(procedure):

    for repo_procedure in build_procedure_list(with_update=False):
        if repo_procedure.lower() == procedure.lower():
            return repo_procedure

    for repo_procedure in build_procedure_list(with_update=True):
        if repo_procedure.lower() == procedure.lower():
            return repo_procedure

    raise ValueError("No matching procedure found")


def change_procedure(procedure, update_channels=True):
    """Switches git branch to the procedure selected
    """

    procedure = _case_match_procedure(procedure)

    with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
        change_branch(procedure)

    if update_channels:
        with WorkingDirectory(settings.CHANNELS_CHECKOUT_DIRECTORY):
            print("Retrieving updates to channels repository")
            subprocess.call(["git", "pull", "-q"])


def save_working_changes(message, initial=False, procedure_code=None):
    """Commits and pushes with the current changes to the repo
    """
    validate_save()

    try:
        with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
            if commit_working_changes(message, settings.PROCEDURE_CHECKOUT_DIRECTORY):
                if initial:
                    print('Performing initial push to repository')
                    subprocess.check_output(['git', 'push', '-q', '--set-upstream', 'origin', procedure_code])
                else:
                    pull_and_merge()
                    print('Pushing to repository')
                    subprocess.check_output(['git', 'push', '-q'])
            else:
                print('No changes detected.')

    except subprocess.CalledProcessError:
        print('Could not commit/push the changes.')
        raise


def generate_review_document_with_display(output_dir, number_of_commits_shown):

    number_of_commits_shown = number_of_commits_shown or 5

    all_commits = get_commits_for_procedure()
    if not all_commits:
        raise Exception("No commits fould please ensure your work has been saved")

    display_commits = all_commits[:number_of_commits_shown]
    message = (
        "\nEnter the number of the version you want to generate review "
        "doc for (0 to cancel):"
    )
    selected_commit = get_user_commit_selection(message, display_commits)

    if selected_commit:
        generate_review_document_for_commit(selected_commit.id, output_dir)


def generate_review_document_for_commit(commit_id, output_dir=None):

    with UsingCommit(commit_id):
        generate_review_document(output_dir)


def generate_review_document(output_dir):

    output_dir = output_dir or settings.DEFAULT_REPORT_LOCATION

    if not node_installed():
        raise RuntimeError("Please install Node.js for your platform from: https://nodejs.org/en/download/")

    if not os.path.isdir("{report_folder}/node_modules".format(report_folder=settings.REPORT_FOLDER)):
        install_studio_report_tool()

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    print("Start building report")
    process = subprocess.Popen(
        [
            "node",
            settings.REPORT_SCRIPT,
            "--endpoint={endpoint}".format(endpoint=settings.REPORT_ENDPOINT),
            "--procedure={procedure}".format(procedure=get_procedure_code()),
            "--output={output_dir}".format(**locals()),
        ],
        stdout=subprocess.PIPE,
    )

    (output) = process.communicate()
    print(output)
    process.wait()


def save_channel_changes(message):
    """Commits and pushes with the current changes to the repo
    """

    try:
        with WorkingDirectory(settings.CHANNELS_CHECKOUT_DIRECTORY):
            if commit_working_changes(message, settings.CHANNELS_CHECKOUT_DIRECTORY):
                pull_and_merge()
                print('Pushing changes to repository')
                subprocess.check_output(['git', 'push', '-q'])
            else:
                print('No changes detected.')

    except subprocess.CalledProcessError:
        print('Could not commit/push the changes.')
        raise


def commit_working_changes(message, checkout_directory):

    with WorkingDirectory(checkout_directory):
        subprocess.check_output(['git', 'stage', '.'])
        output, _ = get_command_output(['git', 'commit', '-a', '-m', '"' + message + '"'])

    return 'nothing to commit' not in output


def publish(selected_commit):
    """ Publishes the procedure with a git note containing the distribution group to the chosen commit
    """

    all_commits = get_commits_for_procedure()
    with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):

        try:
            clear_similar_historical_notes(selected_commit, all_commits)
            edit_note(selected_commit)
        except Exception:
            print('Could not publish the procedure to the specified distribution group.')
            raise


def publish_with_display(dist_groups, number_of_commits_shown):

    with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
        dist_groups = dist_groups or "TS-Testing"  # Default distribution group
        number_of_commits_shown = number_of_commits_shown or 10  # Default number of commits shown

        current_module = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).strip()

        if "Public" in dist_groups.split(","):
            print("\n")
            if not get_yes_no(
                "Are you sure you want to publish {} to Public? [y/N]: ".format(
                    current_module
                )
            ):
                print("Aborting publish to Public")
                sys.exit(1)
        else:
            print("Current module: {}".format(current_module))

        all_commits = get_commits_for_procedure()
        if not all_commits:
            raise Exception("Either there were no previous commits or you set the optional '--number' argument to be "
                            "zero. Please either save your work first or input a positive integer to the --number "
                            "argument.")

        display_commits = all_commits[:int(number_of_commits_shown)]
        message = "\nEnter the number of the version you want to publish here (0 to cancel):"
        selected_commit = get_user_commit_selection(message, display_commits)

        if selected_commit:
            dist_groups = dist_groups.replace(' ', '')
            try:
                publish(selected_commit.copy_with_new_note(dist_groups))
            except UpdateNoteError as e:
                print(e)
                print("-- Publish Failed --")
            else:
                print("-- Publish Successful --")


def delete_unstaged_changes():
    """Deletes all unstaged changes
    """
    try:
        with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
            print('Deleting local changes')
            subprocess.check_output(['git', 'checkout', '-q', '.'])
    except Exception:
        print("Could not delete local changes.")
        raise


def has_unstaged_changes():
    """Returns whether or not there are uncomitted changes
    """
    try:
        with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
            response, _ = get_command_output(['git', 'status', '-s'])
            return True if response else False
    except Exception:
        print("Could not retrieve the git diff. Please ensure the git repo is setup correctly")
        raise


def create_procedure_branch(procedure):
    """ Creates a new branch for the given procedure_code
    """
    for remote_procedure in build_procedure_list():
        if remote_procedure.lower() == procedure.lower():
            print('Git is case sensitive, the procedure {} already exists.\n The procedure you tried to create - {} - '
                  'has the same name.\n Please either correct the case of the procedure or create a new procedure with'
                  ' a different name.'.format(remote_procedure, procedure))
            raise ProcedureCreationError

    try:
        with WorkingDirectory(settings.PROCEDURE_CHECKOUT_DIRECTORY):
            print('Switching to master branch')
            subprocess.check_output(['git', 'checkout', '-q', 'master'])
            print('Creating branch: {}'.format(procedure))
            subprocess.check_output(['git', 'branch', procedure])
            change_procedure(procedure)
    except Exception:
        print("Unable to create a new procedure with name {}".format(procedure))
        raise


def pull_and_merge():
    """ Try a git pull and request user input to decide how a merge conflict is resolved if there is one
    """
    # Find the author of any potential merge conflicts
    try:
        print("Performing git pull")
        subprocess.run(["git", "-c", "protocol.version=2", "pull", "-q"], check=True)
    except subprocess.CalledProcessError:
        # Ask the user which commit they would like to keep
        diff = subprocess.Popen(['git', 'diff'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(diff.communicate()[0])
        print("\n" + "There is a merge error.")
        print("Someone made a commit that conflicts with yours.")
        print("Would you like to accept your changes or theirs?")
        print("Type 'MINE' or 'THEIRS' to choose." + "\n")
        sys.stdout.flush()
        user_input = get_input()
        try:
            if user_input.lower() == "mine":
                subprocess.check_output(['git', 'checkout', '--ours', '.'])
                subprocess.check_output(['git', 'add', '.'])
                subprocess.check_output(['git', 'commit', '-a', '-m', 'merge'])
            elif user_input.lower() == "theirs":
                subprocess.check_output(['git', 'checkout', '--theirs', '.'])
                subprocess.check_output(['git', 'add', '.'])
                subprocess.check_output(['git', 'commit', '-a', '-m', 'merge'])
            else:
                print('\n' + 'Please enter either "MINE" or "THEIRS" to resolve the merge conflict.' + '\n')
                pull_and_merge()
        except subprocess.CalledProcessError:
            print('\n' + 'Something went wrong while trying to merge, please try again or contact pipeline for support'
                  + '\n')
            exit(1)
