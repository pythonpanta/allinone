package Array;

public class countofEvenOdd {
    public static void main(String[] args) {
        int[] arr = {3, 5, 6, 9, -1, 8, 0, 1};
        int evenCount = 0;
        int oddCount = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]%2==0)
                evenCount++;
            else
                oddCount++;

        }

        System.out.println("Number of Even Integers in an Array: "+evenCount);
        System.out.println("Number of odd Integers in an Array: "+oddCount);
    }
}
