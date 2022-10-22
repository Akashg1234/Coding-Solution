# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_length_values(self,head):

        if not head:return 0
        temp,l,arr=head,0,[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
            l+=1
        return l,arr

    def create_tree(self,start,end,arr):

        if start>end:return None

        mid = (start+end)//2
        print(mid)
        new_node = TreeNode(arr[mid])

        new_node.left = self.create_tree(start,mid-1,arr)
        new_node.right = self.create_tree(mid+1,end,arr)
        return new_node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return head

        treeRoot = TreeNode()
        l,arr = self.get_length_values(head)
        print(arr)
        treeRoot = self.create_tree(0,l-1,arr)
        
        return treeRoot

        
        
