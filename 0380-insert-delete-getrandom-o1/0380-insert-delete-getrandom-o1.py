
        
class RandomizedSet:

    def __init__(self):
        self.set_var = set()  

    def insert(self, val: int) -> bool:
        if val in self.set_var:
            return False  
        self.set_var.add(val)
        return True  

    def remove(self, val: int) -> bool:
        if val not in self.set_var:
            return False  
        self.set_var.remove(val)
        return True 
    
    def getRandom(self) -> int:
        if not self.set_var:
            return None  
        return random.choice(list(self.set_var))  

rand_set=RandomizedSet()
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()