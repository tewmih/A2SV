class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()
        five = 0
        ten  = 0
        tewenty = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                five+=1
            elif bills[i] == 10:
                ten +=1
            # else:
            #     tewenty += 1
            if bills[i] - 5 == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
                # ten += 1
            elif bills[i] - 5 == 15:
                if ten>0 and five>0:
                    ten -= 1
                    five -= 1
                    # tewenty += 1
                elif five > 2:
                    five -= 3
                    # tewenty += 1
                else:
                    return False
        return True
