class Solution:
    def checkingforduplicates(self , nums):
        """I will use a set ,
A set does not store duplicates , there it can check for duplicates
"""
        return len(nums) != len(set(nums))

solution = Solution()
nums= [1,3,4,56,1]
results = solution.checkingforduplicates(nums)
print(results)
