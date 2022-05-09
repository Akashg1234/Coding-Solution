# class solution
class Solution:
  
  def __init__(self,arr,m):
    self.arr=arr
    self.m=m
    
  def solve(self):
#     sort the array to get minimum and maximum value's differance
    self.arr.sort()
  
    max_diff = self.arr[len(aelf.arr)-1]-self.arr[0]
    
    for i in range(len[self.arr]-m+1):
      max_diff = min(max_diff, self.arr[i+m-1]-self.arr[i])
      
    return max_diff
  
arr = [12, 4, 7, 9, 2, 23, 25, 41,
          30, 40, 28, 42, 30, 44, 48, 
          43, 50]
m = 7 # Number of students

sol = Solution(arr,m)
print(sol.solve())
