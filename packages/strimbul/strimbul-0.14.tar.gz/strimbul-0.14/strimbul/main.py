# main.py
import sys
sys.path.append(".")

from strimbul.new_page import print_new_page
import streamlit as st

def main():
    st.title("Streamlit App")
    print_new_page()

if __name__ == "__main__":
    main()