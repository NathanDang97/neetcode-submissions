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
    int maxDepth(TreeNode* root) {
        if (!root) {
            return 0;
        }

        queue<TreeNode*> q;
        q.push(root);
        int depth = 0;

        while (!q.empty()) {
            depth++;
            int currLevelSize = q.size();
            for (int i = 0; i < currLevelSize; i++) {
                TreeNode* currNode = q.front();
                q.pop();
                if (currNode->left) {
                    q.push(currNode->left);
                }
                if (currNode->right) {
                    q.push(currNode->right);
                }
            }
        }

        return depth;
    }
};
