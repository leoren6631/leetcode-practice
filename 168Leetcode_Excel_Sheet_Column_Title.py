class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        excel = ''
        while n > 0:
            n-=1
            excel = chr(n%26 + 65) + excel
            n/=26
        return excel
        """
        :type n: int
        :rtype: str
        """
        #first try, limit n in (1,702)
        '''
        excel = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for i in range(1,28):
            if 26*(i-1) < n <= 26*i:
                if i != 1:
                    return excel[i-2] + excel[n-26*(i-1)-1]
                    break
                else:
                    return excel[n-1]
                    break
            elif n > 702:
                return None
        '''