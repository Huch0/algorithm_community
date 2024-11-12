class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        value = str(bin(x^y))
        return(value.count('1'))
        