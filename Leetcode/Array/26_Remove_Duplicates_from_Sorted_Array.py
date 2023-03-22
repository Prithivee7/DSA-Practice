class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        place_holder = 0 
        for i in range(1,len(nums)):
            if nums[i] != nums[place_holder]:
                place_holder += 1
                nums[place_holder] = nums[i]
        return place_holder+1