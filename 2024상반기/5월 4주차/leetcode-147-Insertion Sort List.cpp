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
    ListNode* insertionSortList(ListNode* head) {
        ListNode beforeSortedHead(0);
        ListNode* beforeSortedHeadptr = &beforeSortedHead;

        while (head) {
            ListNode* beforecur = &beforeSortedHead;
            ListNode* cur = beforecur->next;
            while (true) {
                if (cur == nullptr || cur->val >= head->val) break;
                beforecur = beforecur->next;
                cur = cur->next;
            }
            ListNode* term = head;
            head = head->next;
            beforecur->next = term;
            term->next = cur;
        }
        return beforeSortedHead.next;
    }
};