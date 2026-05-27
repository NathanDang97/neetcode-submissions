class Solution {
public:
    // bfs solution, O(rows * cols) time and space
    int bfs(vector<vector<int>>& grid, int r, int c) {
        int rows = grid.size();
        int cols = grid[0].size();
        int directions[4][2] = {
            {-1, 0}, {1, 0}, {0, -1}, {0, 1}
        };
        queue<pair<int, int>> q;
        q.push({r, c});
        int size = 1;
        grid[r][c] = 0;

        while (!q.empty()) {
            auto curr_node = q.front();
            int curr_row = curr_node.first;
            int curr_col = curr_node.second;
            q.pop();
            for (int i = 0; i < 4; i++) {
                int new_row = curr_row + directions[i][0];
                int new_col = curr_col + directions[i][1];
                if (new_row >= 0 && new_row < rows && new_col >= 0 && new_col < cols && grid[new_row][new_col] == 1) {
                    q.push({new_row, new_col});
                    grid[new_row][new_col] = 0;
                    size++;
                }
            }
        }
        return size;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        int maxArea = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    maxArea = max(maxArea, bfs(grid, r, c));
                }
            }
        }
        return maxArea;
    }
};
