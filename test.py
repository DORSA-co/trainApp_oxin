from threading import Thread
import time

class thread_test:
    def __init__(self):
        self.threads = []
        self.n_threads = 1

    def thread_func(self):
        for i in range(10):
            a = 5
            b = 4
            print(a+b)
        return True

    def create_threads(self):
        self.threads = []
        for n in range(self.n_threads):
            self.threads.append(Thread(target=self.thread_func)) 

    def start_threads(self):
        for t in self.threads:
            t.start()

    def stop_threads(self):
        for t in self.threads:
            t.join()

    def start(self):
        self.create_threads()
        self.start_threads()

    def stop(self):
        self.stop_threads()

if __name__=='__main__':
    cls = thread_test()
    # t = time.time()
    # for i in range(10):
    #     cls.start()
    #     cls.stop()
    # print((time.time() - t)*1000)

    t = time.time()
    cls.start()
    cls.stop()
    print((time.time() - t)*1000)