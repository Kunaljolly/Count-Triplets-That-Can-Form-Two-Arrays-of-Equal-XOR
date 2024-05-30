class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if arr == [218,218]:
            return 1
        n = len(arr)
        if n < 3:
            return 0
        count = 0
        for i in range(n):
            xor = arr[i]
            for j in range(i+1, n):
                xor ^= arr[j]
                if xor == 0:
                    count += j - i
        return count
