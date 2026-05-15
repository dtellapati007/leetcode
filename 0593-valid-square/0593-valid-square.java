import java.util.*;
class Solution {
    public int square(int[] a,int[] b){
       int x = (a[0]-b[0]) *  (a[0]-b[0]);
        int y = (a[1]-b[1]) *  (a[1]-b[1]);
        return x + y;
    }
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        Set<Integer> set = new HashSet();
        set.add(square(p1,p2));
        set.add(square(p1,p3));
        set.add(square(p1,p4));
        set.add(square(p2,p3));
        set.add(square(p2,p4));
        set.add(square(p3,p4));
        if(!set.contains(0) && set.size() == 2){
            return true;
        }
        else{
            return false;
        }
    }
}