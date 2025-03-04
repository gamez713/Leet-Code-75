# Problem 643. Maximum Average Subarray

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sums = sum(nums[:k])
        averageArray = []
        averageArray.append(sums / k)

        for i in range(k, len(nums)):
            sums = sums - nums[i - k] + nums[i]

            averageArray.append(sums/k)

        return max(averageArray)

if __name__ == '__main__':
    solution = Solution()

    nums = [1,12,-5,-6,50,3]
    k = 4
    # Output: 12.75000

    result = solution.findMaxAverage(nums, k)
    print(result)