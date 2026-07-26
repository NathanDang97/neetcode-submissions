class Solution:
    # top-down DP solution, O(n^2) time, O(n) space
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        curr_row = [1]
        prev_row = self.getRow(rowIndex - 1)

        for i in range(1, rowIndex):
            curr_row.append(prev_row[i] + prev_row[i - 1])

        curr_row.append(1)
        return curr_row

        