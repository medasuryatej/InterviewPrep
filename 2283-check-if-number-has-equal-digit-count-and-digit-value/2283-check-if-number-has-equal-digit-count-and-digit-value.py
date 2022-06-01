class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            charAtPos = num[i]
            # print(f'index={i}, char-{charAtPos}, counter-{c[f"{i}"]}')
            if int(num[i]) != c[f"{i}"]:
                return False
        return True