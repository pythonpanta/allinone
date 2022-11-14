package functions;

public class BalancedArray {
    public static boolean balancedArray(int[] arr){
        for (int i = 0; i < arr.length; i+=2) {
            if(arr[i]%2!=0)
                return false;
        }
        for (int i = 1; i <arr.length ; i+=2) {
            if (arr[i]%2==0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int[] arr = {0,1,2,3,4,5,6,7,8,9};
        if (balancedArray(arr))
            System.out.println("Balanced");
        else
            System.out.println("Not Balanced");
    }

}
