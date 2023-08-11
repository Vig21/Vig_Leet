# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str)-> int:
#         return self.helper(text1,text2,0,0)
#     def helper(self, text1, text2,i,j) :
#         # i , j are the pointers to the end of text1,text2
#         if i<0 or j<0: #base case if no string or common
#             return 0
#         elif text1[i] == text2[j]: #if both the nth element are same count it
#             return 1 + self.helper(text1,text2,i+1,j+1)
#         else: #text1[i]!=text2[j]
#             return max(self.helper(text1,text2,i+1,j),self.helper(text1,text2,i,j+1)) #remove from either and consider the higher common between the two
    

class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            m = len(s1)
            n = len(s2)
            dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            return self.helper(s1, s2, 0, 0,dp)
            
        def helper(self, s1, s2, i, j,dp):
            if dp[i][j] < 0: #initially -1 if no operation is performed in that state
                if i == len(s1) or j == len(s2):#initially the common subsequence at the nth point is 0
                    dp[i][j] = 0
                elif s1[i] == s2[j]:
                    dp[i][j] =  1 + self.helper(s1, s2, i + 1, j + 1,dp)
                else:
                    dp[i][j] = max(self.helper(s1, s2, i+1, j,dp), self.helper(s1, s2, i, j + 1,dp))
            return dp[i][j]
        
        