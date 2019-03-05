# -*- coding: UTF-8 -*-
from threading import Thread, currentThread

class MyThread(Thread):
    def __init__(self,n):
        if n != "":
            super(MyThread, self).__init__(name=n) #重构run函数必须要写
        else:
            super(MyThread,self).__init__()

    def run(self):
        print("name:%s\n" %self.getName()) #获取名称

if __name__=="__main__":
    t1=MyThread("")
    t2=MyThread("t2")

    t1.start()
    t2.start()
    print(currentThread().getName()) #获取当前线程的名字