class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        # encode length of string and delimeter
        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            # use two pointers
            j = i

            # extract the length of the word
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])

            # extract the word
            i = j + 1
            j = i + word_len
            word = s[i:j]
            decoded.append(word)

            # move the first pointer to the delimeter
            i = j

        return decoded
