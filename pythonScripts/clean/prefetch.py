import os
import shutil
from pathlib import Path

def clear_prefetch_files():
    # Path to the Windows Prefetch directory
    prefetch_dir = Path("C:/Windows/Prefetch")
    
    # Check if the directory exists
    if not prefetch_dir.exists():
        print("Prefetch directory not found.")
        return

    print(f"Attempting to clear files in Prefetch Directory: {prefetch_dir}")
    
    try:
        for item in prefetch_dir.iterdir():
            try:
                if item.is_file():
                    item.unlink()  # Attempt to delete file
                    print(f"Deleted prefetch file: {item}")
                elif item.is_dir():
                    shutil.rmtree(item)  # Attempt to delete directory if any exist
                    print(f"Deleted prefetch folder and its contents: {item}")
            except Exception as e:
                print(f"Could not delete {item}: {e}")
        print("Completed clearing Prefetch Directory.")
    except Exception as e:
        print(f"Could not access Prefetch Directory: {e}")

if __name__ == "__main__":
    clear_prefetch_files()
