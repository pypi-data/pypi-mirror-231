import subprocess
import time

from pypipr.ibuiltins.get_filemtime import get_filemtime
from pypipr.iconsole.print_log import print_log


def auto_reload(filename):
    mtime = 0
    last_mtime = 0
    cmd = f"python {filename}"

    try:
        print_log("Start")
        while True:
            last_mtime = mtime
            subprocess.run(cmd, shell=True)
            while mtime == last_mtime:
                time.sleep(1)
                mtime = get_filemtime(filename)
            print_log("Reload")
    except KeyboardInterrupt:
        print_log("Stop")


if __name__ == "__main__":
    from pypipr.ifunctions.iargv import iargv

    if f := iargv(1):
        auto_reload(f)
