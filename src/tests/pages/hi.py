import os
import signal
import subprocess
from time import sleep

if __name__ == '__main__':
    print(os.getcwd())
    process = subprocess.Popen(
        "cd ../../..; streamlit run src/python/app.py",
        stdout=subprocess.PIPE,
        shell=True,
        preexec_fn=os.setsid
    )
    sleep(4)
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
