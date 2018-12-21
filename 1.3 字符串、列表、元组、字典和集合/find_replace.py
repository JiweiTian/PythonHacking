#find
str1="the quieter you become, the more you are able to hear"
print(str1.find('become'))
print(str1.index('become'))
print(str1)

str2=str1.replace('become','are')
print(str2)

import re
strinfo=re.compile('become')
str3=strinfo.sub('are',str1)
print(str3)