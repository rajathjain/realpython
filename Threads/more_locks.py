import threading 

lock = threading.RLock()
lock.acquire()
lock.acquire()
# Protected - Only owner thread can access
lock.release()
print(lock)