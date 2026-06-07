class Solution {
public:
    // Solution using Dijkstra's, time O(ElogV), space O(E + V)
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        unordered_map<int, vector<pair<int, int>>> graph;
        for (const auto& time : times) {
            graph[time[0]].push_back({time[1], time[2]});
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;
        minHeap.push({0, k});
        unordered_set<int> visited;
        int total_time = 0;

        while (!minHeap.empty()) {
            auto curr_edge = minHeap.top();
            minHeap.pop();
            int curr_weight = curr_edge.first;
            int curr_node = curr_edge.second;
            if (visited.find(curr_node) != visited.end()) {
                continue;
            }
            visited.insert(curr_node);
            total_time = curr_weight;

            for (const auto& next_edge : graph[curr_node]) {
                int next_node = next_edge.first;
                int weight = next_edge.second;
                int next_weight = curr_weight + weight;
                if (visited.find(next_node) == visited.end()) {
                    minHeap.push({next_weight, next_node});
                }
            }
        }

        return visited.size() == n ? total_time : -1;
    }
};
