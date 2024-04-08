def jobs(j):
    j=sorted(j,key=lambda x:x[2],reverse=True)
    m=max(j,key=lambda x:x[1])[1]
    schedule=[-1]*m
    profit=0
    for job in j:
        for i in range(job[1]-1,-1,-1):
            if schedule[i]==-1:
                schedule[i]=job[0]
                profit=profit+job[2]
                break
    return schedule,profit
j1=(1,3,30)
j2=(2,2,20)
j3=(3,3,50)
j=[j1,j2,j3]
x,y=jobs(j)
print(x)
print(y)