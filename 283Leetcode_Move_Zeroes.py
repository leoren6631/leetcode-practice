'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        
        j = 0
        temp = tuple(nums)
        zero = 0
        for i in temp:
            print i
            if j < len(nums):
                print nums
                if i == 0:
                    nums.append(nums.pop(zero))
                    zero+=1
                    print ('zero is ',zero)
                j+=1
        print nums
        """
        index = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index+=1
        for j in xrange(index,len(nums)):
            nums[j] = 0
        print nums
                
            
        
mysolution = Solution()
nums = [1,0,0]


mysolution.moveZeroes(nums)
            