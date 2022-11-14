package loop;

import java.util.Scanner;

public class countPNZ {
    public static void main(String[] args) {
        int positive=0,negative=0,zeros=0;
        char choice;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Enter a Number:");
            int num = sc.nextInt();
            if(num>0)
                positive++;
            else if (num<0)
                negative++;
            else
                zeros++;

            System.out.println("Want to continue: press (y) ");
            choice = sc.next().charAt(0);
        }while (choice=='y');

        System.out.println("Count of positive Numbers: "+positive);
        System.out.println("Count of negative Numbers: "+negative);
        System.out.println("Count of zeros: "+zeros);
    }
}
