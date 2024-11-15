import os
import tempfile
import shutil
from pathlib import Path

def clear_temp_files():
    # Clear user-specific temp folder (usually %temp%)
    user_temp_dir = Path(tempfile.gettempdir())
    clear_directory(user_temp_dir, "User Temp Directory")

    # Clear system-wide temp folder (usually C:\Windows\Temp)
    system_temp_dir = Path("C:/Windows/Temp")
    clear_directory(system_temp_dir, "System Temp Directory")

def clear_directory(directory, directory_name):
    print(f"Clearing files in {directory_name}: {directory}")
    try:
        for item in directory.iterdir():
            try:
                if item.is_file():
                    item.unlink()  # Remove file
                    print(f"Deleted file: {item}")
                elif item.is_dir():
                    shutil.rmtree(item)  # Remove directory and contents
                    print(f"Deleted folder and its contents: {item}")
            except Exception as e:
                print(f"Could not delete {item}: {e}")
        print(f"Completed clearing {directory_name}.")
    except Exception as e:
        print(f"Could not access {directory_name}: {e}")

if __name__ == "__main__":
    clear_temp_files()
