/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    
    ListNode* mergeNodes(ListNode* head) {
        
        if(head==nullptr)return head;
        if(head->next==nullptr)return head;
        
        ListNode *newHead= new ListNode(),*curr=head,*temp=newHead;
        
        int res=0;
        
        while(curr){
            if(curr->val==0){
                if(newHead->next==nullptr && res==0){
                    curr=curr->next;
                }
                else{
                    temp->next=new ListNode(res);
                    temp=temp->next;
                    res=0;
                    curr=curr->next;
                }
            }
            else{
                res+=curr->val;
                curr=curr->next;
            }
        }
        return newHead->next;
        
    }
};
