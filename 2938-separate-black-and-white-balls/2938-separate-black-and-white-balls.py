class Solution:
    def minimumSteps(self, s: str) -> int:
        count=0
        l=0
        r=len(s)-1
        zero_flag=False
        count=0
        zero_count=0
        for i in range(r,-1,-1):
            if zero_flag and s[i] == '1':
                count+=zero_count
                # zero_count=0

            if s[i] =='0':
                zero_flag=True
                zero_count+=1
            
        return count


            