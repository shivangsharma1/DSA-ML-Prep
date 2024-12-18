class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s)+1)]

        for row in range(len(s)+1):
            dp[row][0] = 1

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                #when char are equal: 1 conds, to take the char or not to take the char
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    #when char are not equal
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
                

s= "rabbbit"
t = "rabbit"

obj = Solution()
print(obj.numDistinct(s, t))
