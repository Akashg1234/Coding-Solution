# vestigan of a matrix
t=int(input())
o=1
while o<=t:
    
    N=int(input())
    k=0;countr=countc=0
    arr = []
    
    for i in range(N):
        a=[]
        for j in range(N):
            a.append(int(input()))
        arr.append(a)    
    print(arr)
    for i in range(N):
        for j in range(N):
            if i==j:
                k+=arr[i][j]

    for i in range(N):
        j=0
        if arr[i].count(arr[i][j])>1:
            countr+=1
            continue
        else:
            j+=1
    
    for i in range(N):
        j=0
        if arr[j].count(arr[j][i])>1:
            countc+=1
            continue
        else:
            j+=1
    
    print(f"Case #{o}: {k} {countr} {countc}")            
    o+=1     
