package Array;

import java.util.ArrayList;
import java.util.Arrays;

public class ArrayListToArray {
    public static void main(String[] args) {
        ArrayList<Integer> al = new ArrayList<>();
        al.add(1);
        al.add(4);
        al.add(6);
        al.add(2);
        al.add(3);
        al.add(9);

        int[] arr = new int[al.size()];

        for (int i = 0; i < arr.length; i++) {
            arr[i]= al.get(i);
        }

        System.out.println("ArrayList: "+al);
        System.out.println("Array: "+Arrays.toString(arr));
    }
}
