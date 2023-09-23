from setuptools import setup, find_packages

setup(
    name='strimbul',
    version='0.17',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
    ],
    entry_points={
        'console_scripts': [
            'strimbul=strimbul.__init__:main_init',
        ],
    },
)