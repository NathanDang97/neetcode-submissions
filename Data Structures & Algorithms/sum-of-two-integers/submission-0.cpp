class Solution {
public:
    int getSum(int a, int b) {
        // repeat until the carry bit is 0
        while (b != 0) {
            int carry = (a & b) << 1; // a AND b tells where both bits are 1, 
                                    // shifting left by 1 to move the carry to the correct position (i.e. the next higher bit)
            a = a ^ b; // a XOR b gives the bit-by-bit sum ignoring carry
            b = carry;
        }

        return a;
    }
};
