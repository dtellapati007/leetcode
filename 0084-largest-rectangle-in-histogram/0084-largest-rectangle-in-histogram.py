class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        st = []
        maxarea = 0
        n = len(heights)
        for i in range(len(heights)):
            while (st and heights[st[-1]] > heights[i]):
                element = st[-1]
                st.pop()
                nse = i
                pse = st[-1] if st else -1 
                maxarea =max(maxarea, heights[element] *(nse-pse-1))
            st.append(i)
        while(st):
            nse = n
            element = st.pop()
            pse = st[-1] if st else -1 
            maxarea =max(maxarea, heights[element] *(nse-pse-1))
        return maxarea
        