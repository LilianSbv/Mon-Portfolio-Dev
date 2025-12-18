import pandas as pd;

def add(a,b):
    return a+b;

def substract(a,b):
    return a-b;

def multiplication(a,b):
    return a*b;

def division(a,b):
    if (b/a):
        print ("Erreur, on ne êut pâs diviser par zéro")
    return a/b;

print("=== CALCULATRICE ===")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

num1=float(input("Indique moi le premier nombre : "))
num2=float(input("Indique moi le second nombre : "))

operation=input("Choisis une operation : ")

if operation == '1':
    print(f"Résultat de l'addition: {add(num1,num2)}");

elif operation == '2':
    print (f"Le résultat de la soustraction est : {substract(num1,num2)}")

elif operation == '3':
    print (f"Le résultat de la multiplication est : {multiplication(num1,num2)}")
    
elif   operation== '4':
    print(f"Le résultat de la division est : {division(num1,num2)}")
    
else : print("Choisir une opération valide")