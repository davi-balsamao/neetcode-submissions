from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (max(Counter(nums).values(), default=0) > 1):
            return True
        return False


        