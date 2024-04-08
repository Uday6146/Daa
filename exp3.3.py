def strmatch(a,b):
    n=len(a)
    m=len(b)
    c=0
    for i in range(n-m+1):
        j=0
        c+=1
        while j<=m-1 and a[i+j]==b[j]:
            j+=1
            if j==m:
                return i,c
    return -1,c
a=input("enter string:")
b=input("enter substring:")
i,c=strmatch(a,b)
print(f" sindex {i} with {c} comparisions")
