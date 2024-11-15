import os

scripts = ['2.1.py', '2.2.py', '2.3.py' , '2.py' , '3.1.py' , '3.2.py' , '9.1.py' , '17.1.py' , '17.2.py' , '18.1.py' , '18.2.py' , '18.3.py' , '18.4.py' , '18.5.py' , '18.6.py' , '18.7.py' , '18.8.py' , '18.9.py' , '19.1.py' , '19.2.py' , '19.3.py' , '19.4.py' , 'ae.py']

for script in scripts:
    print(f"Running {script}...")
    os.system(f"python {script}")
    print("Done!")