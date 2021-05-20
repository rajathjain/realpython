import concurrent.futures
import time

def myfunc(name):
    print(f'my func started with {name}')
    time.sleep(10)
    print(f'my func ended with {name}')
    return

if __name__ == '__main__':
    print("main begins")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(myfunc,["foo","bar","pass"])
    print("main ends")        