//We have to calculate the percentage of marks obtained in three subjects (each out of 100) by student A
// and in four subjects (each out of 100) by student B. Create an abstract class 'Marks' with an abstract method
// 'getPercentage'. It is inherited by two other classes 'A' and 'B' each having a method with the same name which
// returns the percentage of the students. The constructor of student A takes the marks in three subjects as its
// parameters and the marks in four subjects as its parameters for student B. Create an object for each of the two
// classes and print the percentage of marks for both the students.


        package Abstraction;

import java.util.Scanner;

abstract class Percentage{
    float math,science,computer,dsa;

    abstract float getPercentage();
}
class X extends Percentage{

    X(float m, float s, float c){
        this.math=m;
        this.science=s;
        this.computer=c;
    }
    @Override
    float getPercentage() {
        return ((this.math+this.science+this.computer)/300*100);
    }
}

class Y extends Percentage{
    Y(float m, float s, float c, float d) {
        this.math=m;
        this.science=s;
        this.computer=c;
        this.dsa=d;
    }

    @Override
    float getPercentage() {
        return ((this.math+this.science+this.computer+this.dsa)/400*100);
    }
}

public class Result {
    public static void main(String[] args) {
        float xm,xs,xc,ym,ys,yc,yd;
        Scanner sc = new Scanner(System.in);
        do{
            System.out.println("Enter mark of X in subject math");
            xm = sc.nextInt();
        }while (xm>100);
        do{
            System.out.println("Enter mark of X in subject computer");
            xc = sc.nextInt();
        }while (xc>100);

        do{
            System.out.println("Enter mark of X in subject Science");
            xs = sc.nextInt();
        }while (xs>100);

        X x = new X(xm,xs,xc);
        System.out.println("the percentage of X is: "+x.getPercentage());

        do{
            System.out.println("Enter mark of Y in subject math");
            ym = sc.nextInt();
        }while (ym>100);
        do{
            System.out.println("Enter mark of Y in subject computer");
            yc = sc.nextInt();
        }while (yc>100);

        do{
            System.out.println("Enter mark of Y in subject Science");
            ys = sc.nextInt();
        }while (ys>100);

        do{
            System.out.println("Enter mark of Y in subject dsa");
            yd = sc.nextInt();
        }while (yd>100);

        Y y = new Y(ym,ys,yc,yd);
        System.out.println("the percentage of Y is: "+y.getPercentage());
    }
}
