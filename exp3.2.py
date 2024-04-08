def seqsearch(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1
a=list(map(int,input("enter list").split(",")))
k=int(input("search key:"))
print(seqsearch(a,k))