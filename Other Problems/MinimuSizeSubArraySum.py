# Problem 209. Minimum Size Subarray Sum

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        sum = 0
        minSubArr = float('inf')

        while right < len(nums):
            sum += nums[right]

            while sum >= target:
                minSubArr = min(minSubArr, right - left + 1)
                sum -= nums[left]
                left +=1

            right += 1

        return minSubArr if minSubArr != float('inf') else 0
    
if __name__ == '__main__':

    target = 7
    nums = [2,3,1,2,4,3]

    # target = 4
    # nums = [1,4,4]

    solution = Solution()

    print(solution.minSubArrayLen(target, nums))