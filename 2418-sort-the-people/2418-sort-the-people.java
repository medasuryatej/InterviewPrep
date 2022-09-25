class Solution {
    public String[] sortPeople(String[] n, int[] h) {
        List<pair> A=new ArrayList<pair>();
        for(int i=0;i<n.length;i++){
            A.add(new pair(h[i],n[i]));
        }
        Collections.sort(A,(a,b)->b.first-a.first);
        for(int i=0;i<n.length;i++){
            n[i]=A.get(i).second;
        }return n;
    }
    
}
class pair{
        int first;
        String second;
        pair(int first,String second){
            this.first=first;
            this.second=second;
        }
    }