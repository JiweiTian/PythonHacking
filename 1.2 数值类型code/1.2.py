a=0o101
print("a="+str(a))
b=64
print('b='+str(b))
c=-237
print('c='+str(c))
d=0x80
print('d='+str(d))
e=-0x92
print('e='+str(e))

print(bool(1))
print(bool(True))
print(bool('0'))
print(bool([]))
print(bool((1,)))

foo=42
bar=foo<42
print(bar)
print(bar+10)
print('%s' %bar)
print('%d' %bar)


print(0.0)
print(-777.)
print(-5.5555119)
print(96e3*1.0)
print(-1.609E-19)

print(complex(2,4))
print(1.23e-045+6.7e+89j)

from decimal import *
print("十进制浮点....")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec +Decimal(.1))

print("转换工厂....")
print(int(4.22222))
print(float(4))
print(complex(4))

print("进制转换....")
print(hex(255))
print(oct(255))
print(oct(0x111))

print("ASII 转换")
print(chr(76))
print(ord('L'))

import math
print(math.ceil(45.33))
print(math.floor(45.33))
print(math.fabs(-45.33))
print(math.factorial(3))
print(math.hypot(2, 2))
print(math.sqrt(4))
print(math.pow(2,3))
print(math.trunc(2.3))
print(math.isnan(5))
print(math.degrees(math.pi))
print(math.radians(180))