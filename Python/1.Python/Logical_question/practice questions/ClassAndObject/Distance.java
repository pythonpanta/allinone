//Add two distances in inch-feet by creating a class named 'AddDistance'.

package ClassAndObject;

import java.util.Scanner;

class AddDistance{
    int feet;
    int inch;

    AddDistance(int f, int i){
        this.feet=f;
        this.inch=i;
    }

    public void sumOfDistance(AddDistance a){
        int newFeet;
        int newInch;
        int tempFeet=this.feet+a.feet;
        int tempInch=this.inch+a.inch;
        newFeet=tempFeet+(tempInch/12);
        newInch=tempInch%12;

        System.out.println("Sum of Distances are: "+newFeet+"."+newInch+" feet");
    }
}

public class Distance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter distance 1: ");
        System.out.print("Feet = ");
        int feet1= sc.nextInt();
        System.out.print("Inch = ");
        int inch1 = sc.nextInt();

        AddDistance a1 = new AddDistance(feet1,inch1);

        System.out.println("Enter distance 2: ");
        System.out.print("Feet = ");
        int feet2= sc.nextInt();
        System.out.print("Inch = ");
        int inch2 = sc.nextInt();

        AddDistance a2 = new AddDistance(feet2,inch2);

        a1.sumOfDistance(a2);
    }
}
