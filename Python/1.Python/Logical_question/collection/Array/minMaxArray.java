package Array;

public class minMaxArray {
    public static void main(String[] args) {
        int[] arr ={3,5 ,6,9 ,8,0,1};
        int max = arr[0];
        int min = arr[1];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>max){
                max=arr[i];
            }
            if(arr[i]<min){
                min=arr[i];
            }
        }
        System.out.println("The max Element of an array is: "+max);
        System.out.println("The min Element of an array is: "+min);
    }
}
