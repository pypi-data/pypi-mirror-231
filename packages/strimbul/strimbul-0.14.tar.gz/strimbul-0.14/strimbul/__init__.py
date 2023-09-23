# from .new_page import print_new_page
from . import new_page
from . import main
import os 

def main_init():
    os.system("streamlit run strimbul/main.py")

if __name__ == "__main__":
    main_init()