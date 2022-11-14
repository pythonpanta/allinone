package Array;

import java.util.HashSet;
import java.util.Set;


public class sum0subArray {
    public static void main(String[] args) {

        Set<Integer> hs = new HashSet<Integer>();

        int[] arr = {-1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9,0,11,12,13};
        int sum=0;
        int count=0;
        for (int i = 0; i < arr.length; i++) {
            sum+=arr[i];
            if (arr[i] == 0 || sum == 0 || hs.contains(sum)){
                count++;
                hs.add(sum);
                }
            }

        System.out.println("there are "+count+" sub arrays whose sum is ZERO");
        }
    }

