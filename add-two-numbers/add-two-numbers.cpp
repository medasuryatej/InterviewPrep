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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode(0);
        ListNode* output = result;
        int carry = 0;
        int opA, opB, sum, mod;
        while (l1 != NULL || l2 != NULL || carry != 0) {
            opA = l1 != NULL ? l1->val : 0;
            opB = l2 != NULL ? l2->val : 0;
            sum = opA + opB + carry;
            carry = sum / 10;
            mod = sum % 10;
            result->next = new ListNode (mod);
            result = result->next; 
            if (l1 != NULL) {
                l1 = l1->next;
            }
            if (l2 != NULL) {
                l2 = l2->next;
            }
        }
        return output->next;
    }
};