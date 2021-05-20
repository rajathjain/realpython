import time
import threading

def myfunc(name):
    print(f'my func started with {name}')
    time.sleep(10)
    print('my func ended')
    return

if __name__ == '__main__':
    print('main started')
    t = threading.Thread(target=myfunc, args=['Real Python'], daemon=True)
    #main thread creating a new thread
    t.start()
    #This statements gets printed before the function call return
    print('main ended')