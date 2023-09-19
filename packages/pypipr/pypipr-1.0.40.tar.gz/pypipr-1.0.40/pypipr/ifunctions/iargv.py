import collections
import sys

iargv = collections.defaultdict(lambda: None)

for k, v in enumerate(sys.argv):
    # Access by Index
    iargv[k] = v

    # Access by Kwargs
    try:
        nk, nv = v.split("=")
        iargv[nk] = nv
    except Exception:
        pass
