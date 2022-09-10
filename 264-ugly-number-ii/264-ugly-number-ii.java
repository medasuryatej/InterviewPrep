class Ugly {
    public int[] num = new int[1690];
    
    Ugly() {
        num[0] = 1;
        int ugly, i2 =0, i3 =0, i5 = 0;
        
        for (int i=1; i<1690; ++i) {
            ugly = Math.min(Math.min(num[i2]*2, num[i3]*3), num[i5]*5);
            num[i] = ugly;
            
            if (ugly == num[i2]*2) ++i2;
            if (ugly == num[i3]*3) ++i3;
            if (ugly == num[i5]*5) ++i5;
        }
    }
    
}

class Solution {
    public static Ugly u = new Ugly();
    public int nthUglyNumber(int n) {
        return u.num[n-1];
    }
}