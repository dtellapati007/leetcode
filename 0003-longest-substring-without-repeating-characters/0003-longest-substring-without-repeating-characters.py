class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =0
        r =0
        leng =0 
        max_len = 0
        n = len(s)
        hash = [-1] * 256
        while(r<n):
            if hash[ord(s[r])]!=-1:
                if hash[ord(s[r])]>=l:
                    l=hash[ord(s[r])] + 1
            leng = r-l+1
            max_len = max(max_len,leng)
            hash[ord(s[r])] = r
            r+=1
        return max_len
