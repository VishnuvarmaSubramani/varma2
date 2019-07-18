N=int(input())
lis=[]
for i in range(2,N+1):
    if(N%i==0):
        lis.append(i)
for j in lis:
    if(j%2==0):
        print(j,end=" ")
