import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

if __name__=='__main__':
    print('当前代码被执行')
else:
    print('当前代码被导入执行')

import myModule

myModule.sayhi()
print('Version',myModule.version)

print(dir(sys))
a=5
print(dir())
del  a
print(dir())

print(sys.version)


import si
print(si.myadd(20,2))
print(si.myminus(20,2))
print(si.mymultiply(20,2))
print(si.mydivision(20,2))
