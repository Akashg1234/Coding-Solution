t=int(input())
op=1;n,k=0,0
q=[];d=[1,2,3]
while op<=t:
    inp=input().split()
    n = int(inp[0])
    if len(inp)>1:
      k = int(inp[1])
      #print(n,"\t",k)

    if n in d:
      if n==1:
          #print(n,"  ",k)
        q.append(k)
        print(q)
      elif n==2:
        q.pop(0)
        print(q)
      elif n==3:
        print(q[0])       
    op+=1
print(q)    
