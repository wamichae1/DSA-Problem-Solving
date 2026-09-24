class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def distance(a,b):

            x = abs(b[0] - a[0])
            y = abs(b[1] - a[1])

            return max(x,y)
        #sum of all distances between each point in points
        return sum(distance(points[i], points[i-1]) for i in range(1, len(points)))

