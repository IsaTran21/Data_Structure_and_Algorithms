class Solution:
    def longestCommonPrefix(self, strs) -> str:
        min_ = strs[0]
        for i in strs:
            if len(i) < len(min_):
                min_ = i
        result = ''
        for i in range(len(min_)):
            count = 0
            for j in strs:
                if j[i] == min_[i]:
                    count+=1
                else:
                    break
            if count == len(strs):
                result += min_[i]
            else:
                break
        return result
if __name__ == "__main__":
    test_1 = Solution()
    test_1_result = test_1.longestCommonPrefix(strs = ["flower","flow","flight"])
    print(test_1_result)
    test_2 = Solution()
    test_2_result = test_2.longestCommonPrefix(strs=["dog", "racecar", "car"])
    print(test_2_result)
