class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:# check if it is less than 10, then return the number
            num = self.newadd(num)
        return num
    def newadd(self, num):# add every digits one by one, calculate the sum
        add = 0
        for i in range(len(str(num))):
            add = int(str(num)[i]) + add
        return add
        
mysolution = Solution()
print mysolution.addDigits(36)

#non-loop version
def add_digits(num):
    x = num % 9
    if not x and num:
        return 9
    else:
        return x
print add_digits(36)