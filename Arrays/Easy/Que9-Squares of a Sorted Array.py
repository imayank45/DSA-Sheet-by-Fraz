# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# brute-force approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted(list(map(lambda x: x**2, nums)))
        return nums
    
    
# optimal approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i,j = 0,n-1
        pos = n-1
        result = [0]*n
        while i<=j:
            if abs(nums[i]) > abs(nums[j]):
                result[pos] = nums[i] * nums[i]
                i+=1
            else:
                result[pos] = nums[j] * nums[j]
                j-=1
            pos -= 1

        return result