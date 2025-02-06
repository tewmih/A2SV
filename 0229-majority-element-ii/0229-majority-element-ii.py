class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        majority_map=dict()
        result=set()

        for num in nums:
            majority_map[num]=majority_map.get(num,0)+1

        check=n//3
        for num in nums:
            if majority_map.get(num)>check:
                result.add(num)
            
        return list(result)