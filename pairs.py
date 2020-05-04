nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
count=0
for i in range(n):
  for j in range(i+1,n):
    if abs(arr[i]-arr[j])==k:
      count+=1
print(count)      
