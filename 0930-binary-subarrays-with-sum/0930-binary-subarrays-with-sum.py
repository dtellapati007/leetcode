class Solution(object):
    def count(self,nums,goal):
        l=0
        r=0
        cnt =0
        sums = 0
        if goal<0:
            return 0
        while(r<len(nums)):
            sums+=nums[r]
            while(sums>goal):
                sums-=nums[l]
                l+=1
            cnt = cnt + (r-l+1)
            r+=1
        return cnt
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.count(nums, goal) - self.count(nums, goal-1)