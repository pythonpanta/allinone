package Array;

import java.util.ArrayList;
import java.util.Arrays;
import static Array.sorting.bubbleSort;

public class removeDuplicate {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,-1,-6,-4,-1,8,7,6,1,2,3,4};
        System.out.println("Array with duplicate elements: "+ Arrays.toString(arr));
        ArrayList<Integer> arr1 = new ArrayList<>();
        bubbleSort(arr);

        for (int i = 0; i < arr.length-1; i++) {
            if(arr[i]==arr[i+1])
                continue;
            else
                arr1.add(arr[i]);
        }
        System.out.println("Array without duplicate elements: " + arr1);
        System.out.println("Size of Array without duplicate elements: " +arr1.size());
    }
}
