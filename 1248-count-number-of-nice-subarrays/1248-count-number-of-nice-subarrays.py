class Solution(object):
    def count(self,nums,goal):
        l=0
        r=0
        cnt =0
        sums = 0
        if goal<0:
            return 0
        while(r<len(nums)):
            sums+=(nums[r]%2)
            while(sums>goal):
                sums-=(nums[l]%2)
                l+=1
            cnt = cnt + (r-l+1)
            r+=1
        return cnt
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.count(nums,k) - self.count(nums,k-1)