class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        tc = Counter(t)
        steps = 0
        for char, freq in sc.items():
            if tc[char] < freq:
                steps += freq - tc[char]
                
        stepsback = 0
        for char, freq in tc.items():
            if sc[char] < freq:
                stepsback += freq - sc[char]
                
        return min(steps, stepsback)
                                       