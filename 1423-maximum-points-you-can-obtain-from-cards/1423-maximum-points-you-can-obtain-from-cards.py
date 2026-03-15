class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lsum =0
        rsum =0
        tsum =0
        rindex = len(cardPoints) - 1
        for i in range(k):
            lsum +=cardPoints[i]
        tsum = lsum
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            rindex-=1
            tsum=max(tsum,lsum+rsum)
        return tsum