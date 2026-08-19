class Solution {
public:
    // aux space solution, O(n) time and space
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        vector<int> paddedFlowerbed(flowerbed.size() + 2);
        for (int i = 0; i < flowerbed.size(); i++) {
            paddedFlowerbed[i + 1] = flowerbed[i];
        }

        for (int i = 1; i < paddedFlowerbed.size() - 1; i++) {
            if (paddedFlowerbed[i - 1] == 0 && paddedFlowerbed[i] == 0 && paddedFlowerbed[i + 1] == 0) {
                paddedFlowerbed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
};