# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#     #check if x is negative
#         if x<0:
#              return False
#     #declaring my variables
#         originals=x
#         reversed_originals= 0
#         #using a while loop to reverse the originals
#         while x !=0:
#             reversed_originals=reversed_originals*10 + (x %10)
#             x //10
#
#         return originals==reversed_originals
#
# s=Solution()
# results=s.isPalindrome(121)

"""
This solution will however exceed the time limited 
to Improve the , we could half the x , reverse it and compare it with original half 
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # check if x is negative
        if x < 0:
            return False

        # declaring my variables
        original = x
        reversed_original = 0
        # using a while loop to reverse the original
        while x != 0:
            reversed_original = reversed_original * 10 + (x % 10)
            x //= 10

        return original == reversed_original


s = Solution()
res = s.isPalindrome(10)
print(res)
