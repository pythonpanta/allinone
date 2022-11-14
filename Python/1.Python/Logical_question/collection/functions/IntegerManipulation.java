package functions;

import java.util.Scanner;

public class IntegerManipulation {
    public static int intManipulate(int a){
        return a*2/4+10;
    }

    public static void main(String[] args) {
        int x;
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a Number: ");
        x = sc.nextInt();
        System.out.println("Manipulated it to: "+intManipulate(x));
    }
}
