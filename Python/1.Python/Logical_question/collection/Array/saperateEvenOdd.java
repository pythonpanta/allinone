package Array;

import java.util.ArrayList;

public class saperateEvenOdd {
    public static void main(String[] args) {
        int[] arr = {3,5 ,6,9 ,8,0,1};
        int[] arr1 = new int[arr.length];
        ArrayList<Integer> even = new ArrayList<>();
        ArrayList<Integer> odd = new ArrayList<>();
        ArrayList<Integer> evenodd = new ArrayList<>();



        for (int i = 0; i < arr.length; i++) {
            if(arr[i]%2==0)
                even.add(arr[i]);
            else
                odd.add(arr[i]);
        }

        for (int j : even) {
            if (!evenodd.contains(j)) {
                evenodd.add(j);
            }
        }
        for (int j : odd) {
            if (!evenodd.contains(j)) {
                evenodd.add(j);
            }
        }

        System.out.println("Separate Even and Odd element: "+evenodd);
    }
}
