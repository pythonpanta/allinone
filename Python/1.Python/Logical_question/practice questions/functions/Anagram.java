package functions;

import java.util.Arrays;
import java.util.Scanner;

public class Anagram {
    public static boolean isAnagram(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        // check if length is same
        if (str1.length() == str2.length()) {

            // convert strings to char array
            char[] charArray1 = str1.toCharArray();
            char[] charArray2 = str2.toCharArray();

            // sort the char array
            Arrays.sort(charArray1);
            Arrays.sort(charArray2);

            // if sorted char arrays are same
            // then the string is anagram
            return Arrays.equals(charArray1, charArray2);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter First String: ");
        String str1 = sc.next();
        System.out.print("Enter Second String: ");
        String str2 = sc.next();
        if(isAnagram(str1,str2)){
            System.out.println(str1 + " and " +str2+" are Anagram");
        }
        else
            System.out.println(str1 + " and " +str2+" are not Anagram");

    }
}
