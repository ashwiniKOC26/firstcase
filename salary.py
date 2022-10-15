salary=int(input("enter the amount"))
y=int(input("enter the year of service"))
if y>=10:
    z=10/100*salary+salary
    print("you will get 10% more bonus",z)
elif y>=6 and y<=10:
    x=8/100*salary+salary
    print("you will get 8% more",x)
elif y<=6:
    c=6/100*salary+salary
    print("you will get 6%",c)
else:
    print("you are not applicable")