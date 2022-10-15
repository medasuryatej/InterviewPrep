class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # referred solution
        cache = {}
        
        def cost_incurred(index, cur_character, run_length, num_deletions_rem):
            if index == len(s):
                # reached end
                return 0
            key = (index, cur_character, run_length, num_deletions_rem)
            if key  in cache:
                return cache[key]
            
            # COST TO DELETE
            delete_the_character_cost = float("inf")
            # are deletions allowed
            if num_deletions_rem > 0:
                delete_the_character_cost = cost_incurred(
                    index + 1,
                    cur_character,
                    run_length,
                    num_deletions_rem - 1
                )
                
            # COST to Keep the character
            cost_to_keep_ch = 0
            # if the cur character is same as prev
            if s[index] == cur_character:
                # potential chance for increase in run_length
                # from 1 to 2, 9 to 10, 99 to 100 etc
                extra_digit_cost = 0
                if run_length == 1 or len(str(run_length + 1)) > len(str(run_length)):
                    extra_digit_cost = 1
                cost_to_keep_ch = extra_digit_cost + cost_incurred(index + 1, cur_character, run_length + 1, num_deletions_rem)
                
            else:
                # new character start
                cost_to_keep_ch = 1 + cost_incurred(index + 1, s[index], 1, num_deletions_rem)
                
            cache[key] = min(delete_the_character_cost, cost_to_keep_ch)
            
            return cache[key]
        
        return cost_incurred(0, "", 0, k)
            