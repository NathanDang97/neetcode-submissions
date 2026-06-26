class Solution {
private:
    int directions[4][4] = {
        {1, 0}, {-1, 0}, 
        {0, 1}, {0, -1}
    };

    void bfs(vector<vector<char>>& grid, int r, int c) {
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int, int>> q;
        grid[r][c] = '0';
        q.push({r, c});
        
        while (!q.empty()) {
            auto curr_node = q.front();
            q.pop();
            int curr_row = curr_node.first;
            int curr_col = curr_node.second;
            for (int i = 0; i < 4; i++) {
                int new_row = curr_row + directions[i][0];
                int new_col = curr_col + directions[i][1];
                if (new_row >= 0 && new_col >= 0 && new_row < rows && new_col < cols && grid[new_row][new_col] == '1') {
                    q.push({new_row, new_col});
                    grid[new_row][new_col] = '0';
                }
            }
        }
    }
public:
    // BFS solution, O(n * m) time and space
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int numIslands = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    numIslands++;
                    bfs(grid, r, c);
                }
            }
        }

        return numIslands;
    }
};
