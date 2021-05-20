import concurrent.futures
import time

class Account:
    def __init__(self) -> None:
        self.balance = 100
        
    def update(self, transaction, amount):
        print(f'{transaction} thread updating')
        local_copy = self.balance
        local_copy += amount
        time.sleep(1)
        self.balance = local_copy
        print(f'{transaction} thread finishing')

if __name__ == '__main__':
    account = Account()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in [('deposit',50),('withdrawal',-150)]:
            ex.submit(account.update,transaction,amount)
    print(f'ending balance is {account.balance}')