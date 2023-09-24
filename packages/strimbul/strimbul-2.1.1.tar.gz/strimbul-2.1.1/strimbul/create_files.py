import os

# List of file names
file_names = ["file1.py", "file2.py", "file3.py", "file4.py", "file5.py"]
plugin_files = ["plugin1.py", "plugin2.py", "plugin3.py", "plugin4.py", "plugin5.py"]
# Loop through the file names
for file_name in file_names:
    # Check if the file exists
    if not os.path.exists(file_name):
        # If it doesn't exist, create the file
        with open(file_name, "w") as file:
            stri = f'import streamlit as st\n\n'
            stri += f'def main():\n\tst.write("This is {file_name}")\n\nif __name__ == "__main__":\n\tmain()'
            file.write(stri)

    print(f"File '{file_name}' exists!")

print("All files are created or already exist.")

# Loop through the file names
for file_name in plugin_files:
    # create a plugin folder if it doesn't exist
    if not os.path.exists("plugins"):
        os.mkdir("plugins")
    # save all the files in the plugin folder
    if not os.path.exists(os.path.join("plugins", file_name)):
        # If it doesn't exist, create the file
        with open(os.path.join("plugins", file_name), "w") as file:
            stri = f'import streamlit as st\n\n'
            stri += f'def main():\n\tst.write("This is {file_name}")\n\nif __name__ == "__main__":\n\tmain()'
            file.write(stri)
