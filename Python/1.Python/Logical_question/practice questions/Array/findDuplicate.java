package Array;
import Array.sorting;

public class findDuplicate {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,-1,-6,-4,-1,8,7,6,1,2,3,4};
        sorting.bubbleSort(arr);
        System.out.println("Duplicate elements are: ");
        for (int i = 0; i < arr.length-1; i++) {
            if(arr[i]==arr[i+1]){
                System.out.print(arr[i]+" ");
            }
        }

    }
}
