package Array;

import java.util.ArrayList;

public class unionIntersection {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int[] arr1 = {7, 8, 9, 10, 11, 12, 13, 14, 15};
        ArrayList<Integer> union = new ArrayList<>();
        ArrayList<Integer> Intersection = new ArrayList<>();

        for (int j : arr) {
            if (!union.contains(j)) {
                union.add(j);
            }
        }
        for (int j : arr1) {
            if (!union.contains(j)) {
                union.add(j);
            }
        }
        System.out.println("Union of two sorted array is: "+union);

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr1.length; j++) {
                if(arr[i]==arr1[j]){
                    Intersection.add(arr[i]);
                }
            }
        }
        System.out.println("Intersection of two array is: "+Intersection);
    }
}
