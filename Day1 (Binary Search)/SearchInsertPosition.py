# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104




class Solution:
    def searchInsert(self, nums, target):
        f=0
        e=len(nums)-1
        while f<=e:
            mid=(f+e)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<=target:
                f=mid+1
            elif nums[mid]>=target:
                e=mid-1
            print(nums)
        return f
        # i = 0
        # j = len(nums) - 1
        # while(i <= j):
        #     pivot = (i + j) // 2
        #     if (nums[pivot] == target):
        #         return pivot
        #     elif (nums[pivot] >= target):
        #         j = pivot - 1
        #     else:
        #         i = pivot + 1
        # return i
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         f=0
#         e=len(nums)-1
# #         if target not in nums:
            
# #             while f<=e:
                
# #                 mid=(f+e)//2
# #                 # if nums[mid]==target:
# #                 # return mid
# #                 if nums[mid]<target:
# #                     e=mid-1
# #                 elif nums[mid]>target:
# #                     f=mid+1
# #                 elif nums[f]<target and nums[e]>target:
# #                     nums.append(target)
      
    

                
            
        
        
                
