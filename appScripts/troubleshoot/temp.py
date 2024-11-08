import os
import shutil
import ctypes
import tempfile

def delete_folder_contents(folder_path):
    """
    Delete all contents of the given folder.
    """
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"Cleared contents of {folder_path}")
    except Exception as e:
        print(f"Error clearing {folder_path}: {e}")

def clear_temp_files():
    print("Starting to clear temporary files...")

    # Temporary folders to clear
    temp_folders = [
        tempfile.gettempdir(),
        os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp'),
        os.path.join(os.environ.get('USERPROFILE', ''), 'AppData', 'Local', 'Temp')
    ]

    for folder in temp_folders:
        delete_folder_contents(folder)

    print("Temporary files cleared successfully.")

def main():
    # Check for administrative privileges
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script requires administrative privileges to run.")
        print("Please run the script as an administrator.")
        return

    clear_temp_files()

if __name__ == "__main__":
    main()
