class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums[:]
        for i in nums:
            result.append(i)
        return result
        # nums.extend(nums)
        # return nums

        # n = len(nums)
        # ans = []
        # for i in range(2 * n):
        #     print(i)
        #     ans.append(nums[i%n])
        # return ans



        