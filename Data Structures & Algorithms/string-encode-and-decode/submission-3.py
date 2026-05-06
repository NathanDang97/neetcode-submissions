class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        # encode length, delimeter, and string
        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            # use two pointers
            j = i

            # extract the length
            while s[j] != "#":
                j += 1
            
            curr_word_len = int(s[i:j])
            
            # move pointers to the actual word
            start = j + 1
            end = start + curr_word_len
            word = s[start:end]
            decoded.append(word)

            # move the first pointer to the start of the next length
            i = end

        return decoded