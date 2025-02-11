class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict=dict()
        for i in range(len(s)):
            my_dict[s[i]]=my_dict.get(s[i],0)+1
        
        # sorted_dict=dict(sorted(my_dict.items(),key=lambda item: item[1],reverse=True))
        my_list=list(my_dict.items())
        for i in range(1,len(my_list)):
            key =my_list[i]
            j=i-1

            while j>=0 and key[1]<my_list[j][1]:
                my_list[j+1]=my_list[j]
                j-=1

            my_list[j+1]=key
        result=[]

        for key,value in reversed(my_list):
            result.append(key*value)
        return "".join(result)

            
        
        
     