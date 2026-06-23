class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        // construct the undirected graph and compute in-degrees of the nodes
        int n = edges.size();
        unordered_map<int, vector<int>> graph;
        vector<int> inDegrees(n + 1, 0);
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
            inDegrees[u]++;
            inDegrees[v]++;
        }

        // run Kahn's algorithm on the graph to trim the in-degrees of the nodes in topological order
        // the nodes with in-degrees > 0 afterwards can form a cycle
        // initialize the queue with nodes having in-degree = 1 since these can't from a cycle
        queue<int> q;
        for (int i = 1; i <= n; i++) {
            if (inDegrees[i] == 1) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int curr_node = q.front();
            q.pop();
            inDegrees[curr_node]--;
            for (const auto& neighbor : graph[curr_node]) {
                inDegrees[neighbor]--;
                if (inDegrees[neighbor] == 1) {
                    q.push(neighbor);
                }
            }
        }

        // traverse the input list of edges in reverse order to find the edge that appears last in the input
        for (int i = n - 1; i >= 0; i--) {
            int u = edges[i][0], v = edges[i][1];
            // if a node u in the topological order has an extra edge to some node v (which forms a cycle)
            if (inDegrees[u] > 1 && inDegrees[v] > 0) {
                return {u, v};
            }
        }
        return {};
    }
};
