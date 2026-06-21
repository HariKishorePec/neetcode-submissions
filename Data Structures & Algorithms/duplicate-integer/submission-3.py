class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [1, 2, 3, 3]
        d = {}
        for i in nums:
            if not d.get(i):
                d[i]=True
            else:
                return True
        return False
