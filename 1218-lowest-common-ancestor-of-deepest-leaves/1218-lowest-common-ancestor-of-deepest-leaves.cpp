/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
struct Info{
    int d;
    TreeNode* node;
};
class Solution {
public:
    Info LCA(TreeNode* root){
        if (!root) return {0, nullptr};
        Info left = LCA(root->left);
        Info right = LCA(root->right);

        if (left.d > right.d)
            return {left.d + 1, left.node};
        else if (right.d > left.d)
            return {right.d + 1, right.node};
        else
            return {left.d + 1, root};
    }
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return LCA(root).node;
    }
};