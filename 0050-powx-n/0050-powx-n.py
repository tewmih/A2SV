class Solution:
    # def half_square(self,x: float, n: int) ->float:
                # n= abs(n)


    def myPow(self, x: float, n: int) -> float:
        # _map = {}
        if n == 0 :
            return 1
        if n < 0:
            x = 1/x
            n = -n
        
        if n%2 == 0:
            half = self.myPow(x,n//2)
            return half*half
        else:
            half = self.myPow(x,n//2)
            return x * half * half
        # if n %2 == 0:
        #     if n<0:
        #         # return (1/self.myPow(x,n//2))*(1/self.myPow(x,ceil(n/2)))
        #         return x * pow(self.myPow(x,n//2),2)
            
        #     else:
        #         # n -= 1
        #         # return self.myPow(x,n//2) * self.myPow(x,ceil(n/2))
        #         return pow(self.myPow(x,n//2),2)
        # else:
        #     if n<0:
        #         # n += 1
        #         # return (1/self.myPow(x,n//2))*(1/self.myPow(x,ceil(n/2)))
        #         return x * pow(self.myPow(x,n//2),2)
            
        #     else:
        #         # n -= 1
        #         # return self.myPow(x,n//2) * self.myPow(x,ceil(n/2))
        #         return pow(self.myPow(x,n//2),2)
            
         