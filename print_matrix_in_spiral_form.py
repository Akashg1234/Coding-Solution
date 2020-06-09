# grnerate random matirx
mat=[]
import random
n=10
m=6
def printInSpiralForm(arr,m,n):
  k=0
  l=0
  #k : starting row index
  #l: starting col index
  #m: ending row index
  #n: starting col index
  while k<m and l<n:

    for i in range(l,n):
      print(arr[k][i],end=" ")
    k+=1
    print("\n")
    for i in range(k,m):
      print(arr[i][n-1],end=" ")
    n-=1
    print("\n")

    if k<m:
      for i in range(n-1,l-1,-1):
        print(arr[m-1][i],end=" ")
      m-=1
      print("\n")
    if l<n:
      for i in range(m-1,k-1,-1):
        print(arr[i][l],end=" ")
      l+=1
      print("\n")
for i in range(m):
  a=[]
  for j in range(n):
    a.append(random.randint(1,10))
  mat.append(a)
for i in range(m):
  for j in range(n):
    print(mat[i][j],end=" ")
  print("\n")
print("\n\n\n")

printInSpiralForm(mat,m,n)

