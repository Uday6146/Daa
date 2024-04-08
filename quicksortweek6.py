def partition(a,l,h):
    i=l
    j=h
    pivot=a[l]
    while(i<j):
        while(a[i]<=pivot and i<h):
            i=i+1
        while(a[j]>pivot and j>=l):
            j=j-1
        if(i<j):
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j

def quick(a,l,h):
    if(l<h):
        loc=partition(a,l,h)
        quick(a,l,loc-1)
        quick(a,loc+1,h)

a=[9,8,7,6,2,3,4,1]
print(a)
quick(a,0,len(a)-1)
print(a)