import os

import fasteners

from .api import Publisher

lock = fasteners.InterProcessLock(os.path.expanduser("~/.tspub.lock"))

__all__ = ["Publisher", "lock"]
