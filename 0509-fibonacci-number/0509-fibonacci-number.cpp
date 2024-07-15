class Solution {
public:
    int f(int n){
        if (n == 0 || n == 1) return n;
        return f(n - 1) + f(n - 2);
    }
    int fib(int n) {
        return f(n);
    }
};