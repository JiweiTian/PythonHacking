dict={'Name':'Zara','Age':7,'Class':'First'}

print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])

#访问不存在的key
#print(dict['Xuanhun'])

#修改值
print("修改前：",dict['Age'])
dict['Age']=8
print("修改后:",dict['Age'])

#删除
del dict['Age']
#print("dict['Age']:",dict['Age'])
dict.clear()
print(dict)

del dict
print(dict)