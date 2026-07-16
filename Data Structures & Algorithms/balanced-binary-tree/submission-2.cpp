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
private:
    int computeHeight(TreeNode* root) {
        if (!root) {
            return 0;
        }
        return 1 + max(computeHeight(root->left), computeHeight(root->right));
    }
public:
    // brute-force solution, O(n^2) time, O(h) space
    bool isBalanced(TreeNode* root) {
        if (!root) {
            return true;
        }

        int leftHeight = computeHeight(root->left);
        int rightHeight = computeHeight(root->right);

        if (abs(leftHeight - rightHeight) > 1) {
            return false;
        }

        return isBalanced(root->left) && isBalanced(root->right);
    }
};
