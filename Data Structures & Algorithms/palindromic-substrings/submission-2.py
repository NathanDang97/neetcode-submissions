class Solution:
    # two pointers solution, time O(n^2)
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        # helper method to count the number of palindromes
        # while "spreading out" the two pointers
        def countPalindromes(left, right):
            num_palindromes = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                num_palindromes += 1
            return num_palindromes

        # the result is given by the number of odd and even length palindromes
        for i in range(len(s)):
            even_palindromes = countPalindromes(i, i + 1)
            odd_palindromes = countPalindromes(i, i)
            count += (even_palindromes + odd_palindromes)

        return count