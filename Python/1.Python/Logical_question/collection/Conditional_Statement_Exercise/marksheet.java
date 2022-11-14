package Conditional_Statement_Exercise;

import java.util.Scanner;

public class marksheet {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int Math = 0;
        while(!(Math>0 & Math<=100)){
            System.out.print("Enter marks in Maths from range 0 to 100:");
            Math=sc.nextInt();
        }
        int CPP = 0;
        while(!(CPP>0 & CPP<=100)){
            System.out.print("Enter marks in C++ from range 0 to 100:");
            CPP=sc.nextInt();
        }
        int DSA = 0;
        while(!(DSA>0 & DSA<=100)){
            System.out.print("Enter marks in DSA from range 0 to 100:");
            DSA=sc.nextInt();
        }
        int DBMS = 0;
        while(!(DBMS>0 & DBMS<=100)){
            System.out.print("Enter marks in DBMS from range 0 to 100:");
            DBMS=sc.nextInt();
        }
        int AI= 0;
        while(!(AI>0 & AI<=100)){
            System.out.print("Enter marks in AI from range 0 to 100:");
            AI=sc.nextInt();
        }

        float total_marks=Math+CPP+DSA+DBMS+AI;
        float percentage=(total_marks/500)*100;

        if(percentage<30)
            System.out.println("Grade C");
        else if(percentage<60&percentage>30)
            System.out.println("Grade B");
        else
            System.out.println("Grade A");


    }
}
