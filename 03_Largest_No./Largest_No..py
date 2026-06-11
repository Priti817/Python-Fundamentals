#Largest no.

a=float(input("enter 1st no.: "))
b=float(input("enter 2nd no.: "))
c=float(input("enter 3rd no.: "))
if a>b and a>c:
    print("Largest no.: ",a)
elif b>a and b>c:
    print("Largest no.: ",b)
else:
    print("Largest no.: ",c)
