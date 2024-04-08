def bindigits(n):
    if n<=1:
        return 1
    else:
        return bindigits(n//2)+1
n=int(input("enter value:"))
print(bindigits(n))