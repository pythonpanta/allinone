package Array;

import java.util.ArrayList;

import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

public class tons_of_array_operation {
    static void even(int[] array){
        System.out.print("Even numbers of An array are: ");
        for (int j : array) {
            if (j % 2 == 0)
                System.out.print(j+" ");
        }
        System.out.println();
    }
    static void odd(int[] array){
        System.out.print("Odd numbers of An array are: ");
        for (int j : array) {
            if (j % 2 != 0)
                System.out.print(j+" ");
        }
        System.out.println();
    }
    static void prime(int[] array){
        System.out.print("Prime numbers of An array are: ");
        for (int i = 0; i < array.length; i++) {
            int count=0;
            for (int j = 2; j <= sqrt(abs(array[i])) ; j++) {
                if(array[i]%j==0)
                    count++;
            }
            if(count==0) {
                System.out.print(array[i]+" ");
            }
        }
        System.out.println();
    }

    static void negative(int[] array){
        System.out.print("Negative numbers of An array are: ");
        for (int j : array) {
            if (j <= 0)
                System.out.print(j+" ");
        }
        System.out.println();
    }

    static void divide_by_five(int[] array){
        System.out.print("Divisible by 5 numbers of An array are: ");
        for (int j : array) {
            if (j%5== 0)
                System.out.print(j+" ");
        }
        System.out.println();
    }

    static void largest(int[] array){
        System.out.print("Largest numbers of An array is:");
        int large=array[0];
        for (int j : array) {
            if (j>large)
                large=j;
        }
        System.out.println(large);
    }

    static void Secondlargest(int[] array){
        System.out.print("Second Largest numbers of An array is:");
        int large=array[0];
        for (int j : array) {
            if (j>large)
                large=j;
        }
        int secondlarge=array[0];
        for (int j : array) {
            if (j>secondlarge&j<large)
                secondlarge=j;
        }
        System.out.println(secondlarge);
    }


    static void Sum(int[] array){
        System.out.print("Sum of numbers of An array is:");
        int Sum = 0;
        for (int j : array) {
            Sum+=j;
        }
        System.out.println(Sum);
    }



    static void sumofprime(int[] array){
        System.out.print("Sum of Prime numbers of An array is: ");
        int sum =0;
        for (int i = 0; i < array.length; i++) {
            int count=0;
            for (int j = 2; j <= sqrt(abs(array[i])) ; j++) {
                if(array[i]%j==0)
                    count++;
            }
            if(count==0) {
                sum+=array[i];
            }
        }
        System.out.println(sum);
    }


    static  void negativearray(int[] array){
        System.out.print("Array of negative element is: ");
       ArrayList<Integer> negativeArray = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            if (array[i]<0)
                negativeArray.add(array[i]);
        }
        System.out.println(negativeArray);
    }

    static  void postiveIncementedArray(int[] array){
        System.out.print("Array of Positive Incremented element is: ");
        ArrayList<Integer> posIncArray = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            if (array[i]>0)
                posIncArray.add(array[i]+1);
        }
        System.out.println(posIncArray);
    }



    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,-1,-2,-3,-4,-5,-6,-7,-8,-9};
        prime(arr);
        largest(arr);
        negative(arr);
        even(arr);
        odd(arr);
        divide_by_five(arr);
        Secondlargest(arr);
        Sum(arr);
        sumofprime(arr);
        negativearray(arr);
        postiveIncementedArray(arr);

    }
}
