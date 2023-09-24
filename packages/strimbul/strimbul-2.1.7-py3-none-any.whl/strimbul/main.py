import streamlit as st

import sys
sys.path.append('..')
# Import all the files
from .file1 import main as file1_app
from .file2 import main as file2_app
from .file3 import main as file3_app
from .file4 import main as file4_app
from .file5 import main as file5_app
from .plugins.plugin1 import main as plugin1_app
from .plugins.plugin2 import main as plugin2_app
from .plugins.plugin3 import main as plugin3_app
from .plugins.plugin4 import main as plugin4_app
from .plugins.plugin5 import main as plugin5_app

# Create a dictionary of all the apps
apps = {
    "file1": file1_app,
    "file2": file2_app,
    "file3": file3_app,
    "file4": file4_app,
    "file5": file5_app,
    "plugin1": plugin1_app,
    "plugin2": plugin2_app,
    "plugin3": plugin3_app,
    "plugin4": plugin4_app,
    "plugin5": plugin5_app
}

# The main function where we will build the actual app
def run():
    # Creates a sidebar
    st.sidebar.title("Navigation")
    # Add a radio button in the sidebar for the selection of apps
    # and store the return value of this radio button in the variable 'selection'
    selection = st.sidebar.radio("Go to", list(apps.keys()))
    # Display the selected app
    app = apps[selection]
    app()

# Call the main function so that your app gets run
if __name__ == "__main__":
    run()