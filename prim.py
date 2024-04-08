inf=999999
n=5
g=[[0,19,5,0,0],
   [19,0,5,9,2],
   [5,5,0,1,6],
   [0,9,1,0,1],
   [0,2,6,1,0]]
snode=[0,0,0,0,0]
nedge=0
snode[0]=True
print("edge:\t weight")
while(nedge<n-1):
    min=inf
    u=0
    v=0
    for i in range(n):
        if snode[i]:
            for j in range(n):
                if (not snode[j] and g[i][j]):
                    if min>g[i][j]:
                        min=g[i][j]
                        u=i
                        v=j
    print(str(u)+" "+str(v)+":\t"+str(g[u][v]))
    snode[v]=True
    nedge+=1
