package Basic_Practice_Question;

import java.util.Scanner;

public class Even_odd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a Number:");
        int num=sc.nextInt();
        if(num%2==0)
            System.out.println("The number is Even.");
        else
            System.out.println("The number is odd.");
    }
}
