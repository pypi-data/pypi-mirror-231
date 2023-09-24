import runpy
import sys
import os

def run():
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    runpy.run_module('strimbul.main', run_name='__main__')
    
if __name__ == "__main__":
    run()