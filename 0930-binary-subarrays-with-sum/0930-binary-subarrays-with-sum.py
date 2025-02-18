class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict={0:1}
        cur_sum=0
        total = 0

        for num in nums:
            cur_sum+=num
            if cur_sum - goal in my_dict:
                total+=my_dict[cur_sum - goal]
            my_dict[cur_sum]=my_dict.get(cur_sum, 0)+1
        
        # if goal ==0:
        #     return (my_dict[0])*(my_dict[0]-1)//2
        # count = 0
        # for key , value in my_dict.items():
        #     if key < goal:
        #         continue
        #     if key-goal in my_dict:
        #         sub = my_dict.get(key-goal)
        #         count+=(sub*value)
        return total