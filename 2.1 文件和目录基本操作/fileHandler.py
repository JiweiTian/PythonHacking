file=open('./test.txt','r')
print(file.read())
file.close()

import os
print(os.getcwd())

print('读取部分内容....')

file=open('./test.txt','r')
print(file.read(2))
file.close()

print('二进制模式....')

file=open('./test.txt','rb')
file.close()

print('逐行读取....')

file=open('./test.txt','r')
for c in file:
    print(c)
file.close()

print('分批读取...')
with open('./test.txt','r') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        print(c)

filePath = './test.txt'

print('a模式写入....')

def printContent(path):
    with open(path,'r') as f:
        print(f.read())

with open(filePath, 'a') as f:
    f.write('追加内容\r\n')

printContent(filePath)

print('w模式写入...')
with open(filePath, 'w') as f:
    f.write("追加内容\r\n")
printContent(filePath)

def removeTest():
    os.remove('./test.txt')

# removeTest()

def renameTxt():
    os.rename('./test.txt','abc.txt')

renameTxt()
