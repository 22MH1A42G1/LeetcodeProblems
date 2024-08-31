struct ListNode* deleteDuplicates(struct ListNode* head){
    if(head==NULL || head->next == NULL)return head;
    struct ListNode *temp=head->next,*lastValidElement=head;
    while(temp!=NULL){
        if(temp->val != lastValidElement->val){
            lastValidElement->next=temp;
           lastValidElement=temp;
        }
        temp=temp->next;
    }
    lastValidElement->next=temp;
    return head;
}