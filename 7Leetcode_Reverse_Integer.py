class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >0:
            y = [i for i in str(x)]
            y.reverse()
            x = int(''.join(y))
        else:
            x = abs(x)
            y = [i for i in str(x)]
            y.reverse()
            x = ''.join(y)
            x = -int(x)
        if x > 2147483647 or x < -2147483648:
            x = 0
        print x
mysl = Solution()
mysl.reverse(123)