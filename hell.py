'''x=str(input(":"))
y=len(x)
if y>3:
    print(x+"ing")
else:
    print(x)'''
a=10
b=5
c=15
d=20
str="a={2},b={0},c={3},d={1}"
print(str.format(c,d,b,a))