//Print the average of three numbers entered by the user by creating a class named 'Average'
// having a method to calculate and print the average.

package ClassAndObject;

import java.util.Scanner;

class Average{
    int a,b,c;

    Average(int x,int y,int z){
        this.a = x;
        this.b = y;
        this.c = z;
    }

    public void displayAverage(){
        int avg = (this.a+this.b+this.c)/3;
        System.out.println("Average of Three number is: "+avg);
    }
}

public class calcAvg {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter three numbers");
        int x = sc.nextInt();
        int y = sc.nextInt();
        int z = sc.nextInt();
        Average a = new Average(x,y,z);
        a.displayAverage();
    }
}
