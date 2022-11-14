package Array;

public class Smallest_positive_missing_nmber {
    public static void main(String[] args) {
        int[] arr ={3,5 ,6,9 ,8,0,1};
        int large = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>large){
                large=arr[i];
            }
        }
        if(large<0)
            System.out.println("The smallest positive missing Number is: "+1);
        else {
            int smpn = large + 1;
            System.out.println("The smallest positive missing Number is: " + smpn);
        }
    }

}
