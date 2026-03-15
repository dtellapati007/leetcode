class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = 0
        leng = 0
        max_len = 0
        zeros=0
        while(r < len(nums)):
            if (nums[r]==0):
                zeros+=1
            if (zeros > k):
                if (nums[l] == 0):
                    zeros-=1
                l+=1
            if (zeros <= k):
                leng = r-l+1
                max_len = max(max_len,leng)
            r+=1
        return max_len

        