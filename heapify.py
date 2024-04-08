def heapify(h,n,i):
    if(n!=1):
        max=i
        l=2*i
        r=2*i+1
        #print(max,l,r)
        if(l<=n and h[max]<h[l] ):
            max=l
        if( r<=n and h[max]<h[r] ):
            max=r
        if(max!=i):
            h[max],h[i]=h[i],h[max]
            heapify(h,n,max)
def heapSort(h,n):
    for i in range((n-1)//2,-1,-1):
        heapify(h,n,i)
    print(h)
    for i in range(n,1,-1):
        h[0],h[i]=h[i],h[0]
        heapify(h,i-1,0)

a=[2,5,1,3]
print(a)
heapSort(a,len(a)-1)
print(a)