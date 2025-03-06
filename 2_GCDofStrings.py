# 1071. Greatest Common Divisor of Strings
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        len1 = len(str1)
        len2 = len(str2)

        if str1 + str2 != str2 + str1:
            return ""
        else:
            while len1 != len2:
                if len1 > len2:
                    len1 -= len2
                else:
                    len2 -= len1
            return str1[:len1]
        
if __name__ == '__main__':
    solution = Solution()
    
    # Example 1:
    # str1 = "ABCABC"
    # str2 = "ABC"

    # Example 2:
    str1 = "ABABAB"
    str2 = "ABAB"

    # Example 3:
    # str1 = "LEET"
    # str2 = "CODE"

    print(solution.gcdOfStrings(str1, str2))