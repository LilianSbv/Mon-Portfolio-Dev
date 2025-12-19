import pandas as pd;

a=0
b=1
nb= int(input("Jusqu'à quel nombre veux-tu que la suite de fibonacci aille ?"))

fib_list=[]

while a<=nb:
        fib_list.append(a)
        temp=a
        a=b
        b=temp+b

print (f"La suite de fibonacci {nb} ")
print (fib_list)

    