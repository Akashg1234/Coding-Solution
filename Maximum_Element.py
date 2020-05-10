# Enter your code here. Read input from STDIN. Print output to STDOUT
#queue using two stack
t=int(input())
op=1;n,k=0,0
q=[];d=[1,2,3]
while t>=1:
    inp=input().split()
    n = int(inp[0])
    if len(inp)>1:
      k = int(inp[1])
      #print(n,"\t",k)

    if n in d:
      if n==1:
          #print(n,"  ",k)
        q.insert(0,k)
        #print(q)
      elif n==2:
        q.pop(0)
        #print(q)
      elif n==3:
        print(max(q))       
    t-=1
#print(q)    
