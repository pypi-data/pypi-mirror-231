import os
import glob

# Get the list of all Python files in the current directory (excluding __init__.py)
modules = [
    os.path.basename(f)[:-3]  # Remove the ".py" extension
    for f in glob.glob(os.path.join(os.path.dirname(__file__), '*.py'))
    if not f.endswith('__init__.py')
]

# Import all modules listed in the 'modules' list
for module in modules:
    __import__(module, globals(), locals())

# Define __all__ to include all the modules
__all__ = modules
