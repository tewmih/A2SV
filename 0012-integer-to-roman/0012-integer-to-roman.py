import math
class Solution:
    def intToRoman(self, num: int) -> str:

        result=''
        while num>0:
            zeros=math.floor(math.log10(num))
            significant=int(num//math.pow(10,zeros))
            base_ten=int((significant)*math.pow(10,zeros))
            print(base_ten)
            if base_ten>=1000:
                result+="M"*significant
            elif base_ten==900:
                result+="CM"
            elif base_ten>=500:
                result+="D"+"C"*int((num-500)/math.pow(10,zeros))
            elif base_ten>= 100:
                result+="C"*significant
            elif base_ten ==90:
                result+="XC"
            elif base_ten>=50:
                result+="L"+"X"*int((num-50)/math.pow(10,zeros))
            elif base_ten == 40:
                result+="XL"
            elif base_ten >=10:
                result+="X"*significant
            elif base_ten >=9:
                result+='IX'
            elif base_ten>=5:
                result=result+"V"+"I"*int(num-5)
            elif base_ten==4:
                result+="IV"
            else:
                result+="I"*num
            print(result)
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0

        return result
        
        