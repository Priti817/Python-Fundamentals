# Prime 

n=int(input("enter a no.: "))
for i in range(2,n):
    if n%i==0:
        print(n,"is not a Prime No.")
        break
else:
    print(n,"is a Prime No.")
