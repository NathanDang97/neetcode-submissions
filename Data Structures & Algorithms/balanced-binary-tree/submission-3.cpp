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
    // for each level, keep track of a tuple {bool : isBalanced, int : currHeight}
    // that is, we compute the current height of the subtree and whether the current subtree is balanced or not
    vector<int> dfs(TreeNode* node) {
        if (!node) {
            return {1, 0};
        }

        vector<int> leftHeight = dfs(node->left);
        vector<int> rightHeight = dfs(node->right);

        bool isBalanced = (leftHeight[0] == 1 && rightHeight[0] == 1) && (abs(leftHeight[1] - rightHeight[1]) <= 1);
        int currHeight = 1 + max(leftHeight[1], rightHeight[1]);

        return {isBalanced ? 1 : 0, currHeight};
    }
public:
    // DFS solution, O(n) time, O(h) space
    bool isBalanced(TreeNode* root) {
        return dfs(root)[0] == 1;
    }
};
