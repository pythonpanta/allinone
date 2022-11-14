//9.Write a program to take an array of strings and display the length of strings in an array.

package Strings;

public class LengthOfStringInArray {
    public static void main(String[] args) {
        String[] arrayOfString = {"Apple", "Ball", "Cat", "Dog", "Elephant"};
        for (String s : arrayOfString) {
            System.out.println("The length of " + s + " is " + s.length());
        }
    }
}
