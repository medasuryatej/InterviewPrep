class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        List<String>[] buckets = new ArrayList[words.length + 1];
        List<String> result = new ArrayList<>();
        for (String w : words)
            count.put(w, count.getOrDefault(w, 0) + 1);

        for (String key : count.keySet()) {
            int freq = count.get(key);
            if (buckets[freq] == null) buckets[freq] = new ArrayList<>();
            buckets[freq].add(key);
        }

        for (int i = words.length; i >= 0 && k > 0; i--) {
            if (buckets[i] == null) continue;
            Trie root = new Trie(buckets[i]);
            List<String> list = root.toList();
            int min = Math.min(k, list.size());
            for (int j = 0; j < min; j++) {
                result.add(list.get(j));
                k--;
            }
        }
        return result;
    }


    class Trie {
        String content;
        Trie[] children = new Trie[26];

        Trie() {
        }

        Trie(List<String> list) {
            for (String element : list) {
                Trie current = this;
                for (char c : element.toCharArray()) {
                    int i = c - 'a';
                    if (current.children[i] == null) current.children[i] = new Trie();
                    current = current.children[i];
                }
                current.content = element;
            }
        }

        List<String> toList() {
            List<String> result = new ArrayList<>();
            getWords(this, result);
            return result;
        }

        private void getWords(Trie node, List<String> list) {
            if (node.content != null) list.add(node.content);

            for (Trie n : node.children) {
                if (n == null) continue;
                getWords(n, list);
            }
        }
    }
}