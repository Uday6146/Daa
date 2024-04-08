def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=list(map(int,input("enter list:").split(",")))
bubblesort(a)
print(a)