'''Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.
'''
class TreeNode(object):
    def __init__(self , x ):
        self.val=x
        self.left =None
        self.right =None
class Solution(object):
    def tosearchTree(self, nums):
         if not nums :
             return  None
    # using divide and conquer
         mid = len(nums)//2

         root =TreeNode(nums[mid])

         root.left= self.tosearchTree(nums[:mid])
         root.right= self.tosearchTree(nums[mid+1:])


         return root




s= Solution()

nums = [-10, -3, 0, 5, 9]
result = s.tosearchTree(nums)


