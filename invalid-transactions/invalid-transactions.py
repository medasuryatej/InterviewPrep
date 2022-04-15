class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        userTransMap = defaultdict(list)
        result = []
        for trans in transactions:
            user, time, amnt, city = trans.split(",")
            userTransMap[user].append([user, int(time), int(amnt), city])
            
        for user in userTransMap:
            # single transaction
            if len(userTransMap[user]) == 1:
                if userTransMap[user][0][2] > 1000:
                    result.append(self.toString(userTransMap[user][0]))
            userTrans = userTransMap[user]
            for i in range(len(userTrans)):
                for j in range(len(userTrans)):
                    if i == j:
                        # same index
                        continue
                    else:
                        # check for price exceeds 1000
                        if userTrans[i][2] > 1000:
                            result.append(self.toString(userTrans[i]))
                            break
                        elif userTrans[i][-1] != userTrans[j][-1]:
                            # different city
                            if abs(userTrans[i][1] - userTrans[j][1]) <= 60:
                                result.append(self.toString(userTrans[i]))
                                break
        return result
                
                            
    def toString(self, trans):
        return f"{trans[0]},{trans[1]},{trans[2]},{trans[3]}"