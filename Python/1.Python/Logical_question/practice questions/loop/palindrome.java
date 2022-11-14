package loop;

import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        System.out.println("Enter a Number");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int a =num;
        int reversedNum = 0;
        while (num!=0){
            int rem = num%10;
            reversedNum=reversedNum*10+rem;
            num=num/10;
        }
        System.out.println("Reversed Number: "+reversedNum);
        if(a==reversedNum)
            System.out.println("is Palindrome");
    }
}
