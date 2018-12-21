#逆序输出一个列表
print("创建列表....")
list_original=['first','second','third','fourth']
length=len(list_original)
print(list_original)
for item in range(length):
    print(list_original[length-1-item])
    print('\n')