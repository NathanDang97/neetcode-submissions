class Solution {
private:
    vector<vector<int>> cache;
public:
    int dfs(int r, int c, vector<vector<int>>& grid, int rows, int cols) {
        if (r == rows || c == cols || grid[r][c] == 1) {
            return 0;
        }
        if (r == rows - 1 && c == cols - 1) {
            return 1;
        }
        if (cache[r][c] != -1) {
            return cache[r][c];
        }

        int steps = dfs(r + 1, c, grid, rows, cols) + dfs(r, c + 1, grid, rows, cols);
        cache[r][c] = steps;
        return steps;
    }

    // top-down DP solution, O(m * n) time and space
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size();
        int cols = obstacleGrid[0].size();

        if (obstacleGrid[rows - 1][cols -1] == 1) {
            return 0;
        }

        cache.resize(rows);
        for (auto& row : cache) {
            row.resize(cols, -1);
        }

        return dfs(0, 0, obstacleGrid, rows, cols);
    }
};