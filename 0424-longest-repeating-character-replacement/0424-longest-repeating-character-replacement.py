class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l =0
        r =0
        hash = [0] * 26
        max_len =0
        maxf =0
        while (r<len(s)):
            hash[ord(s[r])-ord('A')]+=1
            maxf = max(maxf,hash[ord(s[r])-ord('A')])
            if (r-l+1) - maxf > k:
                hash[ord(s[l])-ord('A')]-=1
                maxf =0
                l=l+1
            if (r-l+1) - maxf <= k:
                max_len = max(max_len,r-l+1)
            r+=1
        return max_len

