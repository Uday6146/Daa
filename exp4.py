def insort(a):
    for i in range(1,len(a)):
        v=a[i]
        j=i-1
        while(j>=0 and a[j]>v):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=v
a=[3,1,4,6,22,3,98,0]
insort(a)
print("sorted list:",a)