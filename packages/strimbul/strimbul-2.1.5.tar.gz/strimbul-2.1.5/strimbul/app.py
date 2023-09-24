import subprocess
import os

def run():
    subprocess.Popen(["streamlit", "run", os.path.join(os.path.dirname(__file__), "main.py")])

if __name__ == "__main__":
    run()