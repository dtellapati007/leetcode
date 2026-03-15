class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        lseen = [-1] * 3
        cnt = 0
        for i in range(len(s)):
            lseen[ord(s[i])-ord('a')] = i
            if(lseen[0]!=-1 and lseen[1]!=-1 and lseen[2]!=-1):
                cnt = cnt + (1+min(lseen[0],lseen[1],lseen[2]))
        return cnt
        