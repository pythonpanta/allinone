package functions;

import java.util.Scanner;

public class GDC {
    public static int gdc(int n1, int n2){
        if (n2!=0)
            return gdc(n2,n1%n2);
        else
            return n1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt(), n2 = sc.nextInt();
        int hcf = gdc(n1, n2);

        System.out.printf("G.C.D of %d and %d is %d.", n1, n2, hcf);
    }
}
