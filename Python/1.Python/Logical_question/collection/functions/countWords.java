package functions;

import java.util.Scanner;

public class countWords {
    public static int countWord(String Sentence){
        int count =0;
        for (int i = 0; i < Sentence.length(); i++) {
            if(Sentence.charAt(i)==' ')
                count++;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        String Sentence = sc.nextLine();
        System.out.println("Total Number of Words in sentence: "+(countWord(Sentence)+1));
    }
}
