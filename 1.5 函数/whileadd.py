def sum2(number):
    '''Calculate the sum.

    The number is positive.'''
    sum=0
    n=2
    while n<=100:
        if n%2==0:
            sum=sum+n
        else:
            sum=sum-n
        n+=1
    print(sum)

number=str(input('请输入数字：'))
sum2(number)  
help(sum2)





