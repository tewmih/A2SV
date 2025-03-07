class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)

        total = 0
        for num,freq in cnt.items():
            total += (num +1)*ceil(freq/(num + 1))
        return total