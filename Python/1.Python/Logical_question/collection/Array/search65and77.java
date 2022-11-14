package Array;
import Array.sorting;

public class search65and77 {
    static boolean binarySearch(int[] arr, int target){
        int start=0;
        int end = arr.length-1;
        for (int i = 0; i < arr.length; i++) {
            int mid = start + (end-start)/2;
            if(arr[mid]==target){
                System.out.print(target + " found at index: "+mid);
                return true;
            } else if (arr[mid]<target) {
                start=mid+1;
            }
            else
                end=mid-1;
        }
        return false;
    }
    public static void main(String[] args) {
        int[] arr = {4,6,7,3,57,2,8344,56,21,45,67,65};
        sorting.bubbleSort(arr);
       if(binarySearch(arr,65))
           System.out.println();
       else
           System.out.println(66+" Does not exist in the array");

        if(binarySearch(arr,77))
            System.out.println();
        else
            System.out.println(77+" Does not exist in the array");
    }
}
