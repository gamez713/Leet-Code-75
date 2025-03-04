# Problem 238. Product of Array Except Self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        productArray = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        print(prefix)

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        print(suffix)

        for i in range(n):
            productArray[i] = prefix[i] * suffix[i]

        return productArray


if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3,4]
    # Output: [24,12,8,6]
    #nums = [-1,1,0,-3,3]
    #Output: [0,0,9,0,0]

    print(solution.productExceptSelf(nums))