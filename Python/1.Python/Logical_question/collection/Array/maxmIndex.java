package Array;
import Array.Searching;

public class maxmIndex {
    public static void main(String[] args) {
        int[] arr ={3,5 ,6,9 ,8,0,1};
        int large = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>large){
                large=arr[i];
            }
        }
        Searching.binarySearch(arr,large);
    }
}
