import subprocess
import time
from pathlib import Path


def maybe_pget_weights(url=None, dest="./weights-cache"):
    start = time.time()

    if not Path(dest).exists() and url is not None:
        url = url.replace("gs://", "https://storage.googleapis.com/")
        print("downloading url: ", url)
        print("downloading to: ", dest)
        subprocess.check_call(["pget", "-x", url, dest])
        print("downloading took: ", time.time() - start)
