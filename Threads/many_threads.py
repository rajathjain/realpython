import time
import threading

def myfunc1(name):
    print(f'my func1 started with {name}')
    time.sleep(10)
    print('my func1 ended')
    return

def myfunc2(name):
    print(f'my func2 started with {name}')
    time.sleep(10)
    print('my func2 ended')
    return


def myfunc3(name):
    print(f'my func3 started with {name}')
    time.sleep(10)
    print('my func3 ended')
    return



if __name__ == '__main__':
    print('main started')
    t1 = threading.Thread(target=myfunc1, args=['Real Python'])
    t1.start()
    t2 = threading.Thread(target=myfunc2, args=['foo'])
    t2.start()
    t3 = threading.Thread(target=myfunc3, args=['bar'])
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    #This statements gets printed before the function call return
    print('main ended')