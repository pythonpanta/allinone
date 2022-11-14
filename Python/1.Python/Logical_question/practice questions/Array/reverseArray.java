package Array;

import java.util.Arrays;

public class reverseArray {
    public static void main(String[] args) {
        int[] arr = {-7,-1,-4,9,8,6,4,-3,0,-4,6};
        int[] reversearr = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            reversearr[i]=arr[arr.length-i-1];
        }
        System.out.println("the original array is: "+ Arrays.toString(arr));
        System.out.println("the reversed array is: "+Arrays.toString(reversearr));
    }
}
