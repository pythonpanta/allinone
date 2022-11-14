//Print the sum, difference and product of two complex numbers
// by creating a class named 'Complex' with separate methods for each operation
// whose real and imaginary parts are entered by the user.

package ClassAndObject;

import java.util.Scanner;

class Complex{
    int real;
    int img;

    Complex(int r , int i){
        this.img=i;
        this.real=r;
    }

    public void Addition(Complex c){
        int newReal;
        int newImg;
        newReal = this.real+c.real;
        newImg = this.img+c.img;

        System.out.println("Sum of two complex Number is: "+newReal+" + i"+newImg);
    }

    public void Difference(Complex c){
        int newReal;
        int newImg;
        newReal = this.real-c.real;
        newImg = this.img-c.img;

        System.out.println("Difference of two complex Number is: "+newReal+" + i"+newImg);
    }

    public void Product(Complex c){
        int newReal;
        int newImg;
        newReal = this.real*c.real-this.img*c.img;
        newImg = this.real*c.img+this.img*c.real;

        System.out.println("Product of two complex Number is: "+newReal+" + i"+newImg);
    }


}

public class ComplexOperation {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Real and Imaginary Part of first Complex Number: ");
        System.out.print("Real = ");
        int r = sc.nextInt();
        System.out.print("Imaginary = ");
        int i = sc.nextInt();

        Complex c1 = new Complex(r,i);

        System.out.println("Enter Real and Imaginary Part of Second Complex Number: ");
        System.out.print("Real = ");
        int r1 = sc.nextInt();
        System.out.print("Imaginary = ");
        int i1 = sc.nextInt();

        Complex c2 = new Complex(r1,i1);


        c1.Addition(c2);
        c1.Difference(c2);
        c1.Product(c2);
    }
}
