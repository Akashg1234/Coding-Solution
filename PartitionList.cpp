**
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
    ListNode* partition(ListNode* head, int x) {
        
        ListNode *beforeHead,*afterHead,*before,*after,*temp;
        beforeHead = new ListNode();
        before= beforeHead;
        afterHead = new ListNode();
        after = afterHead;

        temp=head;

        while(temp!=nullptr){
            if(temp->val<x){
                before->next=temp;
                before=before->next;
            }
            else if(temp->val>=x){
                after->next=temp;
                after=after->next;
            }
            temp=temp->next;
        }

        after->next=nullptr;
        before->next=afterHead->next;

        return beforeHead->next;
    }
};
