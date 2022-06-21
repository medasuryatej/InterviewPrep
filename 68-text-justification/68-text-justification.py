class Solution:
    def fullJustify(self, words, maxWidth):
        # res - to store final output
        # cur - to store the current line
        # num_of_letters - to store the non space characters
        res, cur, num_of_letters = [], [], 0
        # iterate over every word
        for w in words:
            # if number of characters + number of words + newWord is more than allowed maxwidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # equal round robin distribution of spaces
                for i in range(maxWidth - num_of_letters):
                    # or 1 here is when len(cur) is 1 (that is only word)
                    cur[i%(len(cur)-1 or 1)] += ' '
                # store the current line in the result
                res.append(''.join(cur))
                # reset
                cur, num_of_letters = [], 0
            # add the word to the current line
            cur += [w]
            # add the word length to number of characters
            num_of_letters += len(w)
        # add the last line left justified to maxwidth, seperated by a single space
        return res + [' '.join(cur).ljust(maxWidth)]