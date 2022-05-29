class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        disc = discount / 100
        for i in range(len(words)):
            word = words[i]
            if word.startswith("$"):
                price = word[1:]
                try:
                    flt_price = float(price)
                    disc_price = flt_price - flt_price * disc
                    words[i] = f"${round(disc_price, 2):.2f}"
                except:
                    continue
        return " ".join(words)