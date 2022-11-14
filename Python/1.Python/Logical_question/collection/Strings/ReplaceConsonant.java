//15.Write a program to replace all consonants from the string
// "Hello, have a good day" with your favourite character.

package Strings;

public class ReplaceConsonant {
    public static void main(String[] args) {
        StringBuilder strr = new StringBuilder();
        String str = "Hello, have a good day";
        char favChar = '$';
        for (int i = 0; i < str.length(); i++) {
            boolean b = str.charAt(i) == 'a'
                    || str.charAt(i) == 'e'
                    || str.charAt(i) == 'i'
                    || str.charAt(i) == 'o'
                    || str.charAt(i) == 'u';

            if (!b && (str.charAt(i) >= 95 && str.charAt(i) <= 122))
                strr.append(favChar);
            else
                strr.append(str.charAt(i));
        }

        System.out.println(strr);
    }
}
