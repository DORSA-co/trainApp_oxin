# SuperFastPython.com
# example of getting the pid of a child process
from time import sleep
from multiprocessing import Process
import os
# function executed in the child process
def task():
    sleep(2)
def run_storage():
    os.system("/bin/python3 ../oxin_storage_management/storage_main_UI.py")
    while True:
        pass
    


# protect the entry point
if __name__ == '__main__':
    # configure the child process
    child = Process(target=run_storage)
    # start the child process
    child.start()
    # get the pid of the child process
    pid = child.pid
    # report the pid
    print(pid)

    while True:
        pass

    # wait for the child process to finish
    child.join()