class Solution {
public:
    int dfs(unordered_set<string> &words, unordered_map<string, int> &wc_map, string currWord) {
        // if word already encountered return its chain len
        if (wc_map.find(currWord) != wc_map.end()) {
            return wc_map[currWord];
        }
        // possible length of currWord
        int possibleLength = 1;
        
        // try truncating one character at a time from current word and recursively do the dfs operation
        // when the truncated word is present in the set
        for (int i=0; i<currWord.length(); i++) {
            string subWord = currWord.substr(0, i) + currWord.substr(i+1);
            if (words.find(subWord) != words.end()) {
                possibleLength = max(possibleLength, 1 + dfs(words, wc_map, subWord));
            }
        }
        wc_map[currWord] = possibleLength;
        
        return possibleLength;
    }
    
    int longestStrChain(vector<string>& words) {
        // referred solution
        // word - chain map
        unordered_map<string, int> word_chainlen;
        // a set to keep track of set of words
        unordered_set<string> wordSet;
        
        for (const string &word: words) {
            wordSet.insert(word);
        }
        int lSC = 0;
        // iterate over every word and determine the longest chain
        // formed from that word
        for (const string &word : words) {
            lSC = max(lSC, dfs(wordSet, word_chainlen, word));
        }
        return lSC;
    }
};