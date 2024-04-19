class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)] # (row, element), (element, column), (what box it's in)
        return len(res) == len(set(res))