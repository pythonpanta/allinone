package Array;

public class DiffrenceBetweenLargestandSmallest {
    public static void main(String[] args) {
        int[] arr ={3,5 ,6,9 ,8,0,1,-3};
        int large = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>large){
                large=arr[i];
            }
        }

        int smallest=arr[0];
        for (int j : arr) {
            if (j<smallest)
                smallest=j;
        }
        int diffrence = large - smallest;

        System.out.println("Difference between largest and smallest Elements of an array is: "+diffrence);
    }
}
