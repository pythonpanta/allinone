package loop;

import java.util.Scanner;

public class countInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count=0;
        String word ="";
        while (!word.equals("exit")){
            System.out.print("Enter a word: ");
            word = sc.next();
            count++;
        }
        System.out.println("Total number of input: "+(count-1));
    }
}
