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
    ListNode* swapPairs(ListNode* head) 
    {
        //edge case
        if(head==nullptr || head->next==nullptr)
        {
            return head;
        }
        ListNode* first=head;//ptr to store the 1st node to be swapped
        ListNode* second=head->next;//ptr to store the 2nd node to be swapped
        //actual swapping
        first->next=swapPairs(second->next);//eg to make 1->4
        second->next=first;//eg to make 2->1
        return second;//return second as it will contain he head at the end
    }
};
