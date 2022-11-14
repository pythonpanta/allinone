package loop;

import java.util.Scanner;

public class GuessingGame {
    public static void main(String[] args) {
        float random = (float) Math.random()*10;
        int rand = (int)random;
        int guess;
        Scanner sc = new Scanner(System.in);
        System.out.println("make a guess:");
        do {
            guess = sc.nextInt();
            if (guess>rand)
                System.out.println("TOO HIGH, TRY AGAIN!!");
            else if(guess<rand)
                System.out.println("TOO LOW, TRY AGAIN!!");
            else
                System.out.println("WOOOOW YOU GUESSED THE SAME NUMBER THAT I HAD THOUGHT!!!! ");

        }while (guess!=rand);
    }
}
