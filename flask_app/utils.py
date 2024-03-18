import os
def find_env_path():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    root_dir = current_dir
    while root_dir != os.path.dirname(root_dir):  # Check until the root of the file system is reached
        if os.path.isfile(os.path.join(root_dir, '.env')):
            return os.path.join(root_dir, '.env')
        root_dir = os.path.dirname(root_dir)
    raise FileNotFoundError(".env file not found")