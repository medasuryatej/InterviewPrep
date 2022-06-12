/**
 * @param {number[][]} brackets
 * @param {number} income
 * @return {number}
 */
var calculateTax = function(brackets, income) {
    let prev = 0;
    let tax = 0;
    for (let i=0; i < brackets.length; i++) {
        const money = brackets[i][0];
        const percentage = brackets[i][1];
        const payable = Math.min(money, income);
        tax += (payable - prev) * percentage / 100;
        prev = payable;
        if (money > income) {
            return tax;
        }
    }
    return tax;
};