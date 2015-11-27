import threading
import time

class my_thread(threading.Thread):
    def run(self):
        global bi
        time.sleep(1)
        if diao.acquire(1):  # Require resource
            bi = bi + 1
            msg = self.name + ' set bi to ' + str(bi)
            print msg
            diao.acquire()   # Require again before release, dead lock!!
            diao.release()
            diao.release()

bi = 0
diao = threading.Lock()
def test():
    for i in range(5):
        t = my_thread()
        t.start()

if __name__ == '__main__':
    test()
