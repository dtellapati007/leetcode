class Solution(object):
    def func(self,nums,k):
        cnt = 0
        r = l = 0
        mpp = {}
        while(r < len(nums)):
            mpp[nums[r]] = mpp.get(nums[r],0) + 1
            while(len(mpp) > k):
                mpp[nums[l]] -= 1
                if mpp[nums[l]] == 0:
                    del mpp[nums[l]]
                l += 1
            cnt = cnt + (r-l+1)
            r += 1
        return cnt
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.func(nums,k) - self.func(nums,k-1)