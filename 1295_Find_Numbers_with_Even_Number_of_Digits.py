class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            temp_i = str(i)
            length = len(temp_i)
            if length % 2 == 0:
                count += 1
        return count
arr = [123, 12, 333, 2, 12, 1234, 5555, 10]
test = Solution()
print(test.findNumbers(arr))