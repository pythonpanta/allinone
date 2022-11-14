package functions;

import java.util.Scanner;

public class countVowel {
    public static boolean isVowel(Character a) {
        if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = 0;
        String Sentence = sc.nextLine().toLowerCase();
        for (int i = 0; i < Sentence.length(); i++) {
            if (isVowel(Sentence.charAt(i))) {
                count++;
            }
        }
        System.out.println("Total number of vowels in a String is: "+count);
    }
}

