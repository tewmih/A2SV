class ProductOfNumbers:

    def __init__(self):
        self.result = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.result = [1]
        else:
            self.result.append(self.result[-1]*num)
        
    def getProduct(self, k: int) -> int:

        n = len(self.result)
        if k >= n:
            return 0

        return self.result[-1]//self.result[-(k+1)]
    
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)