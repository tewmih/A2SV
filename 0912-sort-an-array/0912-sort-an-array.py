class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        M=max(nums)
        count_array=[0]*(M+1)

        for num in nums:
            count_array[num]+=1
        
        # for i in range(1,M+1):
        #     count_array[i]+=count_array[i-1]
        output_array=[]

        for i in range(len(count_array)):
            output_array.extend([i]*count_array[i])
        return output_array
