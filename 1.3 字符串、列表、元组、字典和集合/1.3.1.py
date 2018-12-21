#声明字符串
str1='Hello World'
str2="helllo 玄魂"
print('声明字符串.....')
print(str1)
print(str2)

#访问字符内容
print('访问字符串.....')
print("str1[0]:",str1[0])
print("str2[1:5]:",str2[1:5])

#字符串操作符
print('字符串操作符')
a="Hello"
b="Python"
print("a+b 输出结果：", a+b)
print("a*2输出结果：", a*2)
print("a[1]输出结果：",a[1])
print("a[1:4]输出结果：",a[1:4])

if ("H" in a):
    print("H在变量a中")
else:
    print("H不在变量a中")

if ("M" not in a):
    print("M不在变量a中")
else:
    print("M在变量a中")
print(r'\n')
print(R'\n')

print("My name is %s and weight is %d kg!"%('玄魂',85))
print("My name is %s and \n weight is %d kg!"%('玄魂',85))

#三引号
print('三引号：')
hi='''hi
i am 玄魂'''
print(hi)