def matc(p,n):
    m=[[0 for i in range(n)] for j in range(n)]
    for i in range(1,n):
        m[i][i]=0
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=99999
            for k in range(i,j):
                cost=m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                m[i][j]=min(cost,m[i][j])
    return m[1][n-1]
p=[1,2,3,4,3]
n=len(p)
c=matc(p,n)
print(c)