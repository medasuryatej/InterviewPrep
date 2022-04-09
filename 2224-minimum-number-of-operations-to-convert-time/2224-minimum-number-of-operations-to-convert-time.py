class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        curH, curM = list(map(int, current.split(":")))
        corH, corM = list(map(int, correct.split(":")))
        ops = 0
        hoursDiff = corH - curH
        if curM > corM:
            hoursDiff -= 1
            minsDiff = 60 - curM + corM
        else:
            minsDiff = corM - curM
        print(hoursDiff, minsDiff)
        totalMinsDiff = (hoursDiff * 60) + minsDiff
        print("Total: ", totalMinsDiff)
        ops = 0
        while (totalMinsDiff > 0):
            if totalMinsDiff >= 60:
                div, mod = divmod(totalMinsDiff, 60)
                # totalMinsDiff %= 60
                ops += div
                totalMinsDiff = mod
            elif totalMinsDiff >= 15:
                # totalMinsDiff %= 15
                div, mod = divmod(totalMinsDiff, 15)
                ops += div
                totalMinsDiff = mod
            elif totalMinsDiff >= 5:
                # totalMinsDiff %= 5
                div, mod = divmod(totalMinsDiff, 5)
                ops += div
                totalMinsDiff = mod
            else:
                ops += totalMinsDiff
                totalMinsDiff = 0
        return ops