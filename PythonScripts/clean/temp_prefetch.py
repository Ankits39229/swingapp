import os
import shutil
from pathlib import Path

def clear_temp_files():
    # Paths to the temporary directories
    temp_paths = [Path(os.getenv("TEMP")), Path("C:/Windows/Temp")]
    
    print("Clearing Temporary Files...")
    for temp_dir in temp_paths:
        if temp_dir.exists():
            print(f"Attempting to clear files in: {temp_dir}")
            for item in temp_dir.iterdir():
                try:
                    if item.is_file():
                        item.unlink()  # Delete the file
                        print(f"Deleted temp file: {item}")
                    elif item.is_dir():
                        shutil.rmtree(item)  # Delete the directory and its contents
                        print(f"Deleted temp folder and its contents: {item}")
                except Exception as e:
                    print(f"Could not delete {item}: {e}")
        else:
            print(f"Temp directory not found: {temp_dir}")
    print("Completed clearing Temporary Files.\n")

def clear_prefetch_files():
    # Path to the Windows Prefetch directory
    prefetch_dir = Path("C:/Windows/Prefetch")
    
    print("Clearing Prefetch Files...")
    if prefetch_dir.exists():
        try:
            for item in prefetch_dir.iterdir():
                if item.is_file():
                    item.unlink()  # Attempt to delete file
                    print(f"Deleted prefetch file: {item}")
                elif item.is_dir():
                    shutil.rmtree(item)  # Attempt to delete directory if any exist
                    print(f"Deleted prefetch folder and its contents: {item}")
        except PermissionError:
            print("Access denied. Please run the script as an administrator to clear the Prefetch files.")
        except Exception as e:
            print(f"An error occurred while clearing Prefetch files: {e}")
    else:
        print("Prefetch directory not found.")
    print("Completed clearing Prefetch Files.\n")

if __name__ == "__main__":
    clear_temp_files()
    clear_prefetch_files()
