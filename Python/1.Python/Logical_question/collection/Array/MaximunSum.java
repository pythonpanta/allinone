package Array;

import java.util.ArrayList;

public class MaximunSum {
    public static void main(String[] args) {
        int[] arr = {3, 5, 6, 9, -1, 8, 0, 1};
        int sum = 0;
        ArrayList<Integer> Sums = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
            Sums.add(sum);
        }
        int maxSum = 0;
        for (int i = 0; i < Sums.size(); i++) {
            if (maxSum < Sums.get(i)) {
                maxSum = Sums.get(i);
            }
        }
        System.out.println("maximum Sum of sub Array: " + maxSum);
    }
}
