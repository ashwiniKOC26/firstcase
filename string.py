a=input("enter a string of 5 word    :")
c=len(a)//2
if len(a)>5:
    print("string is not applicable")
else:
    y=a[0]
    middle=a[c]
    last=a[-1]
    print("the first charater is :",y)
    print("the middle charater is :",middle)
    print("the last charater is :",last)
print("process completed")