class LRUCache {
// solution using built-in libraries
private:
    unordered_map<int, pair<int, list<int>::iterator>> cache;
    list<int> order;
    int capacity;

public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        // if the get is a miss
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        // if the get is a hit
        // remove the key from its current position
        // then put it to the most recent position in the ordering
        order.erase(cache[key].second);
        order.push_back(key);
        cache[key].second = --order.end(); // one step back to the real last node
        return cache[key].first;
    }
    
    void put(int key, int value) {
        // if the key already exists,
        // remove its current position
        if (cache.find(key) != cache.end()) {
            order.erase(cache[key].second);
        }
        // if the capacity is reached
        // remove the least recently used element
        else if (cache.size() == capacity) {
            int lru = order.front();
            order.pop_front();
            cache.erase(lru);
        }
        // update the key-value to the most recently used position
        order.push_back(key);
        cache[key] = {value, --order.end()};
    }
};
