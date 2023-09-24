import subprocess
import os
import runpy
import os

def run():
    file_path = os.path.join(os.path.dirname(__file__), "main.py")
    runpy.run_path(file_path, run_name='__main__')
if __name__ == "__main__":
    run()