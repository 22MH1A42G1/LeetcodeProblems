bool isValid(char * s){
    int n= strlen(s);
    char*stack=(char*)malloc(n*sizeof(char));
    int top=-1;
    int i;
    for(i=0;i<n;i++){
        char c=s[i];
        if((c=='(')||(c=='{')||(c=='[')){
            ++top;
            stack[top]=c;
        }
        else{
            if(top == -1 || (c == ')' && stack[top] != '(') ||
                (c == '}' && stack[top] != '{') ||
                (c == ']' && stack[top] != '[')) {
                free(stack);
                return false;
            }
            top--;
        }
    }
    free(stack);
    return top==-1;
}