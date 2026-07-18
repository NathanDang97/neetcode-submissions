class Solution {
public:
    // solution using a stack, O(n) time and space
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> s;

        for (int &a : asteroids) {
            // check for collision once a negative asteroid is encountered
            while (!s.empty() && a < 0 && s.back() > 0) {
                int diff = s.back() + a;
                // if the top asteroid in the stack is smaller in size, pop the stack
                if (diff < 0) {
                    s.pop_back();
                }
                // if the top asteroid in the stack is bigger in size, ignore the current asteroid
                else if (diff > 0) {
                    a = 0;
                }
                // if the top asteroid and the current one are equal in size, both are destroyed
                else {
                    a = 0;
                    s.pop_back();
                }
            }
            // add an asteroid to the stack if the stack is empty
            // or if it's positive or if the top of the stack is negative
            if (a != 0) {
                s.push_back(a);
            }
        }

        return s;
    }
};