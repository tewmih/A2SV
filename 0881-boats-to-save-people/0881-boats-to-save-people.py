class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def countingSort(arr):
            max_val = max(arr)
            count = [0] * (max_val + 1)
            while len(arr) > 0:
                num = arr.pop(0)
                count[num] += 1
            for i in range(len(count)):
                while count[i] > 0:
                    arr.append(i)
                    count[i] -= 1
            return arr
        arr =countingSort(people)
        left,right=0,1
        count=0
        while left<len(arr) and right<len(arr):
            if arr[left]+arr[right]<=limit:
                count+=1
                left+=2
                right+=2
            elif arr[left]<=limit:
                count+=1
                left+=1 
                right+=1

        if left<len(arr) and arr[left]<limit:
            count+=1
        if right<len(arr) and arr[right]<limit:
            count+=1
        return count

