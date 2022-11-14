package loop;

import java.util.Scanner;

public class largestSmallest {
    public static void main(String[] args) {
        int largest=0,smallest=0;
        char choice;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Enter a Number:");
            int num = sc.nextInt();
            if(num>largest)
                largest=num;
            if (smallest>num)
                smallest=num;

            System.out.println("Want to continue: press (y) ");
            choice = sc.next().charAt(0);
        }while (choice=='y');

        System.out.println("the largest Among the Entered number is: "+largest);
        System.out.println("the smallest Among the Entered number is: "+smallest);

    }
}
