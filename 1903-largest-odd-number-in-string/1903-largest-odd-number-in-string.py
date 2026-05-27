class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        ind = -1
        for i in range(len(num)-1,-1,-1):
            if(int(num[i]) % 2 == 1):
                ind = i
                break
        i = 0
        while i<=ind and num[i] == 0:
            i+=1
        return num[i:ind+1]
        