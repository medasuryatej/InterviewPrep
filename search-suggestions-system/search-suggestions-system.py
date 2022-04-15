class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []
        products.sort()
        for idx, searchChar in enumerate(searchWord):
            tempResult = []
            for product in products:
                # if len(tempResult) > 3:
                #     break
                if idx < len(product) and searchChar == product[idx]:
                    tempResult.append(product)
            output.append(tempResult[:3])
            products = tempResult
        return output
            