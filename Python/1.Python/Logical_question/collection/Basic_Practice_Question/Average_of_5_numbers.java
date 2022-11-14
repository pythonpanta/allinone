package Basic_Practice_Question;

import java.util.Scanner;

public class Average_of_5_numbers {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int sum=0;
        int[] arr = new int[5];
        for (int i = 0; i < arr.length; i++)
            arr[i]=sc.nextInt();
        for (int nums : arr) sum += nums;
        int average=sum/arr.length;
        System.out.println("Average is: "+average);

    }
}
