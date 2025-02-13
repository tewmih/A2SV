class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker=0
        holder=0
        while seeker<len(nums) and holder<len(nums):
            if nums[seeker]!=0 and nums[holder]==0:
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
                seeker+=1
                holder+=1
                continue
            elif nums[seeker]==0:
                seeker+=1
                continue
            seeker+=1
            holder+=1
            

        print(nums)