class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums[:]
        # for i in nums:
        #     ans.append(i)
        # return ans
        # nums.extend(nums)
        # return nums

        n = len(nums)
        ans = []
        for i in range(2 * n):
            print(i)
            ans.append(nums[i%n])
        return ans



        