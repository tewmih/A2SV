class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict=dict()
        s2_dict=dict()

        for i in range(len(s1)):
            s1_dict[s1[i]]=s1_dict.get(s1[i],0)+1
        print(s1_dict)
        left =0
        for i in range(len(s2)):
            if s2[i] in s1_dict:
                s2_dict[s2[i]]=s2_dict.get(s2[i],0)+1
            if i - left + 1 > len(s1):
                if s2[left] in s2_dict:
                    s2_dict[s2[left]] -= 1
                    if s2_dict[s2[left]] == 0:
                        del s2_dict[s2[left]]
                left += 1
            if s1_dict==s2_dict:
                return True
            
        return False
