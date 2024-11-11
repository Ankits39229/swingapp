import os
import subprocess

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get all Python files in the directory
python_files = sorted([f for f in os.listdir(script_directory) if f.endswith('.py')])

# Loop through each Python file and execute it
for python_file in python_files:
    print(f"\nRunning {python_file}:\n" + "=" * 30)
    try:
        # Run the script and capture the output
        result = subprocess.run(['python', os.path.join(script_directory, python_file)], capture_output=True, text=True)
        
        # Print the output of the script
        print(result.stdout)
        
        # Print errors if any
        if result.stderr:
            print("Errors:\n", result.stderr)
    except Exception as e:
        print(f"Failed to run {python_file}: {e}")
