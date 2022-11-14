package functions;

import java.util.Scanner;

public class circumferenceandArea {
    public static void circumferenceArea(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Radius of a  circle:");
        int r = sc.nextInt();
        System.out.println("Circumference of a Circle: "+ 2*3.14*r);
        System.out.println("Area of a circle: "+ 3.14*r*r);
    }

    public static void main(String[] args) {
        circumferenceArea();
    }
}
