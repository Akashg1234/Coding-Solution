n=int(input())
l1=[]
count_list=[]
#this code is contributed
for i in range(n):
  k=int(input())
  #print(k)
  l1.append(k)

for i in range(1,6):
  count_list.append(l1.count(i))
  #[val, idx] = max(count_list); 
print(l1[count_list.index(max(count_list))])
