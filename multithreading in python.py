# Multithreading in Python

from threading import Thread
from time import sleep

class Hi(Thread):
    def run(self):  # sourcery skip: for-index-underscore
        for i in range(5):
            print('hi')
            sleep(0.25)

class Hello(Thread):
    def run(self):  # sourcery skip: for-index-underscore
        for i in range(5):
            print('hello')
            sleep(0.25)

t1 = Hi()
t2 = Hello()

t1.start()
sleep(0.2)
t2.start()

# Ask main thread to complete t1 & t2 threads
t1.join()
t2.join()

print('Bye')
