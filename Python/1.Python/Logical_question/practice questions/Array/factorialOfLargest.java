package Array;

public class factorialOfLargest {
    public static void main(String[] args) {
        int[] arr ={3,5 ,6,9 ,8,0,1};
        int large = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>large){
                large=arr[i];
            }
        }
        System.out.println("The largest Element of an array is: "+large);
        int factorial=1;
        for (int i = 1; i <=large ; i++) {
            if(large==0 || large==1)
                factorial=1;
            else
                factorial*=i;
        }
        System.out.println("Factorial of the largest Number is: "+factorial );
    }
}
