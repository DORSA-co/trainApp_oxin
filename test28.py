import subprocess
import time

process = subprocess.Popen(
            ['/bin/python3', '../oxin_storage_management/storage_main_UI.py', 'en', 'False']
            )

while True:
    print(process.poll())