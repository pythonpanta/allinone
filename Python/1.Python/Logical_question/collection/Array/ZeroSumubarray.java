package Array;

import java.util.HashSet;
import java.util.Set;

class ZeroSumSubarray {
    static Boolean subArrayExists(int[] arr)
    {
        Set<Integer> hs = new HashSet<Integer>();
        int sum = 0;

        for (int j : arr) {
            sum += j;

            if (j == 0 || sum == 0 || hs.contains(sum))
                return true;

            hs.add(sum);
        }

        return false;
    }

    public static void main(String[] arg)
    {
        int[] arr = {-3, 2, 3, 1, 6};

        // Function call
        if (subArrayExists(arr))
            System.out.println(
                    "Found a subarray with 0 sum");
        else
            System.out.println("No Such Sub Array Exists!");
    }
}
