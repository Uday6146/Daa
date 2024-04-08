def fibs(a,x,n):
    f2=0
    f1=1
    f=1
    offset=-1
    while(f<n):
        f2=f1
        f1=f
        f=f1+f2
    while(f>1):
        i=min(offset+f2,n-1)
        if(a[i]<x):
            f=f1
            f1=f2
            f2=f-f1
            offset=i
        elif(a[i]>x):
            f=f2
            f1=f1-f2
            f2=f-f1
        else:
            return i
    if(a[offset+1]==x):
        return offset+1
    else:
        return -1

a=list(map(int,input("enter list:").split(",")))
n=len(a)
x=int(input("enter search key:"))
print("element found at",fibs(a,x,n))
