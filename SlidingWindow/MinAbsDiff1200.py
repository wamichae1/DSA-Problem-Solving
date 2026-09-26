class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # sort, then find min, then add to ans
        arr.sort()
        mini = float("inf")

        for n in range(1, len(arr)):
            mini = min(mini, arr[n] - arr[n-1])
        ans = []

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == mini:
                ans.append([arr[i-1], arr[i]])
        return ans

#single for loop pass, reset list if new min is found
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        mini = float("inf")
        ans = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < mini:
                mini = diff
                ans = [[arr[i-1], arr[i]]]
            elif diff == mini:
                ans.append([arr[i-1], arr[i]])
        return ans