package functions;

import java.util.Scanner;

public class Grade {
    public static String grades(int marks){
        if(marks>90 && marks<=100)
            return "AA";
        else if (marks>80 && marks<=90)
            return "AB";
        else if (marks>70 && marks<=80)
            return "BB";
        else if (marks>60 && marks<=70)
            return "BC";
        else if (marks>50 && marks<=60)
            return "CD";
        else if (marks>40 && marks<=50)
            return "DD";
        else
            return "Fail";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Your Marks: ");
        int mark = sc.nextInt();
        System.out.println("Grade: "+grades(mark));
    }
}
