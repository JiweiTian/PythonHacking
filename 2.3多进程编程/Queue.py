# -*- coding: UTF-8 -*-

from multiprocessing import Process, Queue
import time

def f(q,data):
    q.put(data) #添加数据

def out(q):
    time.sleep(4)
    print(q.get()) #获取数据

if __name__ == '__main__':
    q = Queue() #创建Queue实例
    p = Process(target=f, args=(q,[1,2,3]))
    p.start()

    p.join()

    p1 = Process(target=out, args=(q,))

    p1.start()

    p1.join()