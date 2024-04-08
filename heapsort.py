def heapify(h,n,i):
    if(n!=1):
        max=i
        l=2*i
        r=2*i+1

        if(l<=n and h[l]>h[max]):
            max=l
        if(r<=n and h[r]>h[max]):
            max=r
        if(max!=i):
            h[max],h[i]=h[i],h[max]
            heapify(h,n,max)

def heapsort(h,n):
    for i in range((n-1)//2,-1,-1):
        heapify(h,n,i)
    print(h)
    for i in range(n,1,-1):
        h[0],h[i]=h[i],h[0]
        heapify(h,i-1,0)

a=list(map(int,input("enter list:").split(",")))
print(a)
heapsort(a,len(a)-1)
print(a)