import threading
import time
import stacktracer
stacktracer.trace_start("trace.html")

biA = 1
biA_lock = threading.Lock()  # biA lock
biB = 1
biB_lock = threading.Lock()  # biB lock

def diao1():
    global biA, biB
    print "diao1 acquiring lock biA"
    biA_lock.acquire()       # diao1 start cao biA
    time.sleep(5)            # 5 miao jiu she

    print "diao1 acquiring lock biB"
    biB_lock.acquire()       # diao1 start cao biB
    time.sleep(5)            # 5 miao jiu she
    biA += 5
    biB += 5

    print "diao1 releasing both locks"
    biB_lock.release()
    biA_lock.release()

def diao2():
    global biA, biB
    print "diao2 acquiring lock biB"
    biB_lock.acquire()      # diao2 start cao biB
    time.sleep(5)           # 5 miao she

    print "diao2 acquiring lock biA"
    biA_lock.acquire()      # diao2 start cao biA
    time.sleep(5)           # 5 miao she
    biA += 10
    biB += 10

    print "diao2 releasing both locks"
    biB_lock.release()
    biA_lock.release()

t = threading.Thread(target = diao1)
t.setDaemon(1)
t.start()

t = threading.Thread(target = diao2)
t.setDaemon(2)
t.start()

while 1:
    # Sleep forever
    time.sleep(10)
