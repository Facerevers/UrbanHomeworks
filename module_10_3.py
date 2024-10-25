import threading
from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            account_repl = randint(50, 500)
            self.balance += account_repl
            print(f"Пополнение: {account_repl}. Баланс: {self.balance}.")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            account_withdr = randint(50, 500)
            print(f"Запрос на {account_withdr}")
            if account_withdr <= self.balance:
                self.balance -= account_withdr
                print(f"Снятие: {account_withdr}. Баланс: {self.balance}.")
            else:
                print("Запрос отклонён, недостаточно стредств")
                self.lock.acquire()



bk = Bank(100)

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")