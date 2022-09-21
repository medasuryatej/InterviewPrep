class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int[] output = new int[queries.length];
        int evenSum = 0;
        for (Integer a: nums) {
            if (a%2 == 0) {
                evenSum += a;
            }
        }
        
        for (int i=0; i<queries.length; i++) {
            int index = queries[i][1];
            int val = queries[i][0];
            int newValue = nums[index] + val;
            // even
            // odd
            if (nums[index] % 2 == 0) {
                evenSum -= nums[index];
            }
            if (newValue % 2 == 0) {
                evenSum += newValue;
            }
            output[i] = evenSum;
            nums[index] = newValue;
            // print(nums);
        }
        
        // print(nums);
        return output;
    }
    
    public static void print(int[] array) {
        for (Integer a: array) {
            System.out.print(a + ", ");
        }
        System.out.println("\n");
    } 
}