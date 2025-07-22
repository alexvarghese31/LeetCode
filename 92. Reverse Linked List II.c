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
    ListNode* reverseBetween(ListNode* head, int left, int right) 
    {
        //initialising the dummy node
        ListNode dummy(0);
        dummy.next=head;
        ListNode* prev=&dummy;
        // Step 1: Move `prev` to point to the node before `left`
        for(int i=1;i<left;i++)
        {
            prev=prev->next;
        }
        ListNode* curr=prev->next;//curr points to the leftmost node in reversal 
        for(int i=0;i<right-left;i++)
        {
            //reversal(inplace)
            ListNode* temp=curr->next;
            curr->next=temp->next;
            temp->next=prev->next;
            prev->next=temp;
        }
        return dummy.next;   
    }
};
