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
class Solution {
public:
    // iterarive solution using a stack, O(n) time and space
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> in_order;
        stack<TreeNode*> s;
        TreeNode* curr = root;

        while (curr || !s.empty()) {
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }
            curr = s.top();
            s.pop();
            in_order.push_back(curr->val);
            curr = curr->right;
        }
        return in_order;
    }
};