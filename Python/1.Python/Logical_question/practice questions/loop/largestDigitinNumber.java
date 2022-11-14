package loop;

import java.util.Scanner;

public class largestDigitinNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Number: ");
        int num = sc.nextInt();
        int largest = 0;
        while(num!=0){
            int rem = num % 10;
            if(rem>largest)
                largest=rem;
            num/=10;
        }

        System.out.println("the largest digit in the Number is: "+largest);
    }
}
