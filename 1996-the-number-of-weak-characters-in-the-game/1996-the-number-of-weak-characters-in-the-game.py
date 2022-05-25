class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # referred solution
        # sort based on decreasing attack and increasing defense
        properties.sort(key=lambda prop: (-prop[0], prop[1]))
        # now strong attacks are front
        result = 0
        max_defense = float("-inf")
        for attack, defense in properties:
            if defense < max_defense:
                # found a weak character
                result += 1
            else:
                # update defense.
                # the next charcter defense must be atleast small than this
                max_defense = defense
        return result
        
                