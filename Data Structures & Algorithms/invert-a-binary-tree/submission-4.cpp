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
    // BFS solution, O(n) time and space
    TreeNode* invertTree(TreeNode* root) {
        if (!root) {
            return nullptr;
        }
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* curr_node = q.front();
            q.pop();
            swap(curr_node->left, curr_node->right);
            if (curr_node->left) {
                q.push(curr_node->left);
            }
            if (curr_node->right) {
                q.push(curr_node->right);
            }
        }

        return root;
    }
};
