//2.Write a program to take two string as input and check whether they are equal or not (Try
//both equals and ignore case)

package Strings;

import java.util.Scanner;

public class StringsEqualorNot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputString1 = sc.nextLine();
        String inputString2 = sc.nextLine();
        String a = "Ravi";
        String b = "Ravi";

        if(a == b){
            System.out.println("Reference variable A nad B both are pointing to same object");
        }

        if(inputString1 == inputString2){
            System.out.println("while taking input from the user at the run time two different objects are created");
        }

        if(inputString1.equalsIgnoreCase(inputString2)){
            System.out.println("Two strings are Equal");
        }
    }
}
