package Array;

import java.util.Arrays;
import java.util.Scanner;

public class Insert {
    public static void main(String[] args) {
        int[] arr = {3, 5, 6, 9, -1, 8, 0, 1};
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter index of element to be deleted:");
        int index = sc.nextInt();
        int[] newarr = new int[arr.length + 1];
        for (int i = 0,k=0; i < arr.length; i++) {
            if ((i == index)) {
               newarr[k++]=sc.nextInt();
            }
            newarr[k++]=arr[i];
        }
        System.out.println(Arrays.toString(newarr));
    }
}
