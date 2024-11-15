import subprocess
import os

# Adjust to the directory where your scripts are stored
script_dir = os.path.join(os.getcwd(), 'audit')  
audit = [
    '2.1.py', '2.2.py', '2.3.py', '2.py', '3.1.py', '3.2.py', '9.1.py',
    '17.1.py', '17.2.py', '18.1.py', '18.2.py', '18.3.py', '18.4.py',
    '18.5.py', '18.6.py', '18.7.py', '18.8.py', '18.9.py', '19.1.py',
    '19.2.py', '19.3.py', '19.4.py'
]

for script in audit:
    script_path = os.path.join(script_dir, script)
    print(f"Running {script_path}...")
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        print("Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}:")
        print(e.stderr)
    print("Done!\n")

