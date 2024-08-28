/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *p = l1, *q = l2;
    struct ListNode *result = NULL, *curr = NULL;
    int carry = 0;
    while (p != NULL || q != NULL || carry != 0) {
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        int x = (p != NULL) ? p->val : 0;
        int y = (q != NULL) ? q->val : 0;
        int sum = (carry + x + y) % 10;
        carry = (carry + x + y) / 10;
        newNode->val = sum;
        newNode->next = NULL;
        if (result == NULL) {
            result = curr = newNode;
        } else {
            curr->next = newNode;
            curr = newNode;
        }
        if (p != NULL) p = p->next;
        if (q != NULL) q = q->next;
    }
    return result;
}