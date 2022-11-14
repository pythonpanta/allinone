//10.Write the program to take an array of string input and sort the array according to length of
// string both ascending and descending.

package Strings;

import java.util.Arrays;

public class SortArrayOfString {
    public static void main(String[] args) {
        String[] arrayOfString = {"Apple", "Ball", "Cat", "Dog", "Elephant"};
        for (int i = 0; i < arrayOfString.length; i++) {
            for (int j = 1; j < arrayOfString.length - i; j++) {
                if (arrayOfString[j - 1].length() > arrayOfString[j].length()) {
                    String temp = arrayOfString[j];
                    arrayOfString[j] = arrayOfString[j - 1];
                    arrayOfString[j - 1] = temp;
                }
            }
        }

        System.out.println("Sorted Array of string in Ascending Order");
        System.out.println(Arrays.toString(arrayOfString));

        for (int i = 0; i < arrayOfString.length; i++) {
            for (int j = 1; j < arrayOfString.length - i; j++) {
                if (arrayOfString[j - 1].length() < arrayOfString[j].length()) {
                    String temp = arrayOfString[j];
                    arrayOfString[j] = arrayOfString[j - 1];
                    arrayOfString[j - 1] = temp;
                }
            }
        }

        System.out.println("Sorted Array of string in Descending Order");
        System.out.println(Arrays.toString(arrayOfString));
    }
}
