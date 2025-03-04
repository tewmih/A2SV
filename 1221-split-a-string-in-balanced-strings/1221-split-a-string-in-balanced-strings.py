class Solution:
    def balancedStringSplit(self, s: str) -> int:
        _map = {}
        n = len(s)
        count  = 0
        for i in range(n):
            _map[s[i]] = _map.get(s[i],0)+1
        l_count = 0
        r_count = 0
        for i in range(n):
            if s[i] == 'L':
                l_count+=1
            else:
                r_count+=1
            _map[s[i]] = _map.get(s[i],0)-1
            if _map[s[i]] == 0:
                del _map[s[i]]
            if l_count == r_count:
                count+=1
                _map[s[i]] = _map.get(s[i],0)-l_count
                if _map[s[i]] <= 0:
                    del _map[s[i]]
        return (count)                
