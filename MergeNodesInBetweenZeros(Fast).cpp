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
        
        ListNode *ptr1= head,*ptr2=head->next;
        
        int res=0;
        
        while(ptr2){
            if(ptr2->val==0){
                ptr1=ptr1->next;
                ptr1->val=res;
                res=0;
            }
            else{
                res+=ptr2->val;
            }
            ptr2=ptr2->next;
        }
        ptr1->next=nullptr;
        return head->next;
        
    }
};
