'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        '''
        s_dict = Counter(s)
        t_dict = Counter(t)
        if len(s) != len(t):
            return False
        else:
            return t_dict == s_dict
'''


s = "anagram"
t = "nagaram" 

   
mysolution = Solution()
mysolution.isAnagram(s,t)