def eleuniq(a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                return False
    return True
a=list(map(int,input("enter list:").split(",")))
print(eleuniq(a))