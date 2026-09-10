class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        c = 0
        writer = 0
        seeker = 0
        for i in range(l):           
            if nums[i] != val:
                nums[writer] = nums[i]
                writer += 1
                c += 1  
            print(nums, i)          
        return c

