import random
x=input("enter a choice: rock, paper, scissor   ::  ")
z=["rock","paper","scissor"]
q=random.choice(z)
print(q)
if q==x:
    print("tie")
elif x=="rock":
    if q=="scissor" : print("you won")
    elif q=="paper" : print("you loss")
elif x=="scissor":
    if q=="paper" : print("you won")
    elif q=="rock" : print("you loss")
elif x=="paper":
    if q=="scissor" : print("you won")
    elif q=="rock" : print("you loss")
else:
    print("invalid")
