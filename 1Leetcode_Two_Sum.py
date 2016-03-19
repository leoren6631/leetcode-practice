class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        for i in nums:
            check = target - i
            k = l + 1
            for j in nums[l+1:]:
                if j == check:
                    return (l,k)
                k+=1
            l+=1