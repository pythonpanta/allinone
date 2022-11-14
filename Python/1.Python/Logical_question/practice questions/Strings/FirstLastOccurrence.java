//13.Write a program to find the first and the last
// occurrence of the letter 'o' and character ',' in "Hello, World”.

package Strings;

public class FirstLastOccurrence {
    public static void main(String[] args) {
        String hello = "Hello, World";
        System.out.println("Index of first occurrence of 'o': " + hello.indexOf("o"));
        System.out.println("Index of last occurrence of 'o': " + hello.lastIndexOf("o"));
        System.out.println("Index of first occurrence of ',': " + hello.indexOf(","));
        System.out.println("Index of last occurrence of ',': " + hello.lastIndexOf(","));
    }
}
