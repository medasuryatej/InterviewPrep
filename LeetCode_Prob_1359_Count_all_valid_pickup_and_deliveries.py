class Solution:
    def countOrders(self, n: int) -> int:
        """
        The N orders can be placed in N! ways
        The N delivers can be of below sort
        P1, P2 ------ Pn
        now DN can be placed in only one position after PN
        P1, P2, ---- Pn-1, Pn
        now DN can be placed in three places after Pn-1, after Pn before Dn and
            after Pn , after Dn
        as this progression goes the deliveries follow format
        1 * 3 * 5 --- * 2*(n-1) - 1
        """
        output = 1
        for i in range(n, 0, -1):
            output *= (2*i - 1)
        return (output * Solution.factorial(n)) % (10**9 + 7)
        
    def factorial(num):
        if num < 0:
            return "Invalid Factorial"
        if num <= 1:
            return 1
        return num * factorial(num-1)
