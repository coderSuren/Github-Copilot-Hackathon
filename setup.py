import subprocess

files = ["weather.py"]  # List the Python files you want to convert

for file in files:
    subprocess.call(["pyinstaller", "--onefile", file])