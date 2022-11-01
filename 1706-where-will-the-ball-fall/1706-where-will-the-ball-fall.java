class Solution {
    public int[] findBall(int[][] grid) {
        // referred solution
        // intitution
        // ball can go to next row and next column, only if adjacent cell value is same
        // as current cell value, else it gets stuck
        int result[] = new int[grid[0].length];
        for (int i = 0; i < grid[0].length; i++) {
            result[i] = findBallDropColumn(0, i, grid);
        }
        return result;
    }

    public int findBallDropColumn(int row, int col, int[][] grid) {
        // base case; ball reached the last row
        if (row == grid.length)
            return col;
        // if going right from current col, nextcol would be col + 1
        // if going left from current col, nextcol would be col - 1
        int nextColumn = col + grid[row][col];
        
        if (nextColumn < 0 ||
                nextColumn > grid[0].length - 1 ||
                grid[row][col] != grid[row][nextColumn]) {
            return -1;
        }
        return findBallDropColumn(row + 1, nextColumn, grid);
    }
}