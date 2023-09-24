import subprocess
import os

def run():
    subprocess.call(["streamlit", "run", os.path.join(os.path.dirname(__file__), 'app.py')])

if __name__ == "__main__":
    run()