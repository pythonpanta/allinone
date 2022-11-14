package Array;

public class secondSmallest {
    public static void main(String[] args) {
        int[] array = {1,2,3,4,5,6,7,-1,-6,-4,-1,8,7,6,1,2,3,4};
        System.out.print("Second smallest numbers of An array is:");
        int smallest=array[0];
        for (int j : array) {
            if (j<smallest)
                smallest=j;
        }
        int secondSmallest=array[0];
        for (int j : array) {
            if (secondSmallest>j && j>smallest)
                secondSmallest=j;
        }
        System.out.println(secondSmallest);
    }
}
