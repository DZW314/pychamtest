#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'DZW'
__mtime__ = '2019/7/9'
# code is far away from bugs with the god animal protecting
    I love animals. They are so funny. 
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃   *   ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃ Bless ┣┓
              ┃ NoBUG ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""
import time
import threading
from concurrent.futures import ThreadPoolExecutor
#First Method
def greet_them(people):
    for person in people:
        print("Hello Dear " + person + " . How are you?")
        time.sleep(0.5)

#Second Method
def assign_id(people):
    i = 1
    for person in people:
        print("Hey! {}, your id is {}.".format(person,i))
        i += 1
        time.sleep(0.5)

def print_line1():
    time.sleep(3)
    print('-----1-----')
    print('-----2-----')
    print('-----3-----')
    print('-----4-----')
    print('-----5-----')


def print_line2():
    time.sleep(3)
    print('-----*-----')
    print('-----*-----')
    print('-----*-----')
    print('-----*-----')
    print('-----*-----')


def main():
    print('-------Line-------')
    executor = ThreadPoolExecutor(max_workers=4)
    task1 = executor.submit(print_line1)
    task2 = executor.submit(print_line2)
    print('-------Line-------')


people = ['Richard', 'Mike', 'Jack', 'Leo', 'Nancy']
t = time.time()

t1 = threading.Thread(target=greet_them, args=(people,))
t2 = threading.Thread(target=assign_id, args=(people,))

t1.start()
t2.start()

t1.join()
t2.join()

if __name__ == '__main__':
    main()

print("Woaahh!! My work is finished...")
print("I took " + str(time.time() - t))