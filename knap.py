def knap(w,v,c,n):
    t=[[0 for i in range(c+1)] for j in range(n+1)]
    for i in range(c+1):
        t[0][i]=0
    for i in range(1,n+1):
        for j in range(c+1):
            t[i][0]=0
            if(j<w[i-1]):
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=max(t[i-1][j],v[i-1]+t[i-1][j-w[i-1]])
    return t,t[n][c]
n=int(input("n"))
w=[2,3,4,5]
v=[3,4,5,6]
c=int(input("c"))
z,h=knap(w,v,c,n)
print(z,h)