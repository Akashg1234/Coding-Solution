# Containing duplicate
from collections import defaultdict

def containsDuplicate(nums):
        store=defaultdict(int)
        for i in nums:
            store[i]+=1
        print(store)
        for val in store.values():
          if val>1:
            return True
        return False
print(containsDuplicate(num))
