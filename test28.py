import subprocess
import time
import threading

t = time.time()

def test():
    global t
    print((time.time() - t)*1000)
    print('test')
    t = time.time()
    threading.Timer(0.001, test).start()
    print('after')

test()

# process = subprocess.Popen(
#             ['/bin/python3', '../oxin_storage_management/storage_main_UI.py', 'en', 'False']
#             )

# while True:
#     print(process.poll())