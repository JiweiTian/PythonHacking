a=int(4.5)
print(a)
while True:
    try:
        n=input("请输入一个整数：")
        n=int(n)
        break
    except ValueError as e:
        print("无效数字，再次输入...",e)
print("输入成功！")

import sys
try:
    f=open('intergers.txt')
    s=f.readline()
    i=int(s.strip())
except IOError as e:
    print('I/O error',e)
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise 

print(sys.exc_info()[0])

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast


try:
    s=input('Enter something -->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException as x:
    print('ShortInputException: The input was of length %d, \ was expecting at least %d' % (x.length,x.atleast))
else:
    print('No exception was raised')


def test1():
    try:
        print('to do stuff')
        raise Exception('hehe')
    except Exception:
        print('process except')
        print('to return in except')
        return 'except'
    finally:
        print('to return in finally')
        return 'finally'

test1Return=test1()
print('test1Return:'+test1Return)



class shuruException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
while True:
    try:
        shuru=input('Enter something -->')
        if len(shuru)>5:
            break
        else:
            raise shuruException(len(shuru),5)
    except shuruException as e:
        print('ShortInputException: The input was of length %d, \ was expecting at least %d' % (e.length,e.atleast))
        print("无效输入，再次输入...",e)
print("输入成功！")