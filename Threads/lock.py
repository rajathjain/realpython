import concurrent.futures
import threading
import time

class Account:
    def __init__(self) -> None:
        self.balance = 100
        self.lock = threading.Lock()
        
    def update(self, transaction, amount):
        print(f'{transaction} thread updating')
        self.lock.acquire()
        local_copy = self.balance
        local_copy += amount
        time.sleep(3)
        self.balance = local_copy
        self.lock.release()
        print(f'{transaction} thread finishing')

if __name__ == '__main__':
    account = Account()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in [('deposit',50),('withdrawal',-150)]:
            ex.submit(account.update,transaction,amount)
    print(f'ending balance is {account.balance}')