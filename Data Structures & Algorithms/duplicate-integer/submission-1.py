class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        if len(nums)==0:
            return False
        for i in range(len(nums)):
            dict[nums[i]]=dict.get(nums[i],0)+1
        return max(dict.values())>=2
        