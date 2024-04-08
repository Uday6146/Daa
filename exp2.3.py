def toh(n,s,d,a):
    if n==1:
        print(f"move {s} to {d}")
    else:
        toh(n-1,s,a,d)
        print(f"move {s} to {d}")
        toh(n-1,a,d,s)
n=int(input("enter n value:"))
s='s'
a='a'
d='d'
toh(n,s,d,a)