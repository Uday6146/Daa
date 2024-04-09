def sumofdigits(n):
    s=0
    while(n!=0):
        d=n%10
        s+=d
        n=n//10
    return s
n=int(input("enter value:"))
a=int(input("enter a:"))
b=int(input("enter b:"))
total=a+b
print(a+b)
print(sumofdigits(n))




