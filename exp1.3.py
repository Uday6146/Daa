def minele(a):
    mini=a[0]
    for i in range(len(a)):
        if a[i]<mini:
            mini=a[i]
    return mini
a=list(map(int,input("enter list:").split(",")))
print("minimum element is:",minele(a))