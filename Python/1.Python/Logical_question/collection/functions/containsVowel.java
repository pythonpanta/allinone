package functions;

import java.util.Scanner;

public class containsVowel {
    public  static boolean isVowel(String str){
        for (int i = 0; i < str.length(); i++) {
            if(str.charAt(i) == 'a' || str.charAt(i) == 'e' || str.charAt(i) == 'i' || str.charAt(i) == 'o' || str.charAt(i) == 'u'){
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String Sentence = sc.nextLine();
        System.out.println("Does the string contains vowel letter: "+isVowel(Sentence));
    }
}
