from setuptools import setup, find_packages
# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='strimbul',
    version='2.1.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'strimbul = strimbul.app:run',
        ],
    },
    # new arguments
    long_description=long_description,
    long_description_content_type='text/markdown',
)