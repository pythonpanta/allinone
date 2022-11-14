package Conditional_Statement_Exercise;

import java.util.Scanner;

public class vowel_or_consonant {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter an Alphabet:");
        char c = sc.next().charAt(0);
        int compare1 = Character.compare(c,'a');
        int compare2 = Character.compare(c,'e');
        int compare3 = Character.compare(c,'i');
        int compare4 = Character.compare(c,'o');
        int compare5 = Character.compare(c,'u');

        if(compare1==0|compare2==0|compare3==0|compare4==0|compare5==0)
            System.out.println("Provided Alphabet is vowel");
        else
            System.out.println("Provided Alphabet is Consonant");
    }
}
