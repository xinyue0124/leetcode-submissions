class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 1. path close/open
        # 2. 2n ->complete
        # 3. open < n add open back and recuision
        # 4. close < open add close
        res = []
        path = []
        def backtrack(open, close):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if  open < n:
                path.append('(')
                backtrack(open + 1, close)
                path.pop()
            if close < open:
                path.append(")")
                backtrack(open, close + 1)
                path.pop()
        backtrack(0, 0)
        return res
        