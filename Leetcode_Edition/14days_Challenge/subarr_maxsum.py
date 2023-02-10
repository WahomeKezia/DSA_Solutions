class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # declaring my variables
        # the max_sum starts with the first elemnt of the array and curre_sum is  set to 0
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum += num
            # compares the current sum to max sum
            if curr_sum > max_sum:
                max_sum = curr_sum
                # checks is current sum is negative to reset it
            if curr_sum < 0:
                curr_sum = 0
        return max_sum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
results = s.maxSubArray(nums)
print(results)
