class Solution {
    public boolean checkIfPangram(String sentence) {
        int[] alphabets = new int[26];
        for (int i=0; i <sentence.length(); i++) {
            alphabets[sentence.charAt(i) - 'a']++;
        }
        int sum = 0;
        for (int i =0; i < 26; i++) {
            if (alphabets[i] > 0) {
                sum++;
            }
        }
        return sum==26;
    }
}