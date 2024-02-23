class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """   
        start = 0
        end = 2
        if len(nums) < 2:
            return len(nums)
        
        while end <= len(nums)-1:
            # print(start,end,nums)
            if nums[start] == nums[end]:
                nums.pop(end)
            else: 
                start+=1
                end+=1

            
        return len(nums)
