class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {}
        for i, num in enumerate(nums):
            Diff = target - num
            if Diff in PrevMap:
                return [PrevMap[Diff], i]
            PrevMap[num] = i
        return
        
            




            