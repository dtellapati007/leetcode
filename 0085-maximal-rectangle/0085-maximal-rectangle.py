class Solution(object):
    def largestRectangleArea(self, heights):
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
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix[0])
        arr = [0] * m
        maxarea = 0
        for row in matrix:
            for i in range(m):
                if row[i] == '1':
                    arr[i] +=1
                else:
                    arr[i] = 0
            maxarea = max(maxarea, self.largestRectangleArea(arr))
        return maxarea
        