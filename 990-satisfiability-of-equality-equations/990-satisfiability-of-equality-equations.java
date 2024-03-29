class Solution {
    // referred solution
    // you do a union find
    // have a static array for each character
    static int[] root = new int[26];
    public boolean equationsPossible(String[] equations) {
        
        for (int i=0; i<26; i++) {
            root[i] = i; // let parent of each character be itself
        }
     
        
        int x, y;
        
        for (String eq: equations) {
            if (eq.charAt(1) == '=') { // consider all equalilty equations being connected components, hence their parents being same
                x = eq.charAt(0) - 'a';
                y = eq.charAt(3) - 'a';
                union(x, y);
            }
        }
        
        for (String eq: equations) {
            // for unequal components their parents must not be same
            if (eq.charAt(1) != '=' ) {
                x = eq.charAt(0) - 'a';
                y = eq.charAt(3) - 'a';
                if (find(x) == find(y)) {
                    // if same return false
                    return false;
                }
            }
        }
        return true;
    }
    
    public static int find(int x) {
        if (x != root[x]) {
            root[x] = find(root[x]);
        }
        return root[x];
    }
    
    public static void union(int x, int y) {
        x = find(x);
        y = find(y);
        root[x] = y;
    }
}