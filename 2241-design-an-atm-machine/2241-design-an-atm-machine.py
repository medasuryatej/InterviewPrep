class ATM:
    # refered solution
    def __init__(self):
        self.money = [0,0,0,0,0] # 20, 50, 100, 200, 500
        self.num_denoms = len(self.money)

    def deposit(self, banknotesCount: List[int]) -> None:
        for index, notes in enumerate(banknotesCount):
            self.money[index] += notes

    def withdraw(self, amount: int) -> List[int]:
        withdraw_amount = [0] * 5
        
        for index, denom in enumerate([500, 200, 100, 50, 20]):
            note_idx = self.num_denoms - index - 1
            # either take all notes of a denomination available in the 
            # atm or take a required multiple
            withdraw_amount[note_idx] = min(self.money[note_idx], amount // denom)
            # subtract respective denomination value from the amount
            amount -= withdraw_amount[note_idx] * denom
        if amount == 0:
            # found exact change
            for i in range(self.num_denoms):
                self.money[i] -= withdraw_amount[i]
        return [-1] if amount > 0 else withdraw_amount
            
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)