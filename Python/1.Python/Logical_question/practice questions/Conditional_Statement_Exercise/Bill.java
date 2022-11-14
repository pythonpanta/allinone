package Conditional_Statement_Exercise;

import java.util.Scanner;

public class Bill {
    public static void main(String[] args) {
        System.out.println("1. MoMo veg:          150");
        System.out.println("2. MoMo chicken:      250");
        System.out.println("3. MoMo buff:         200");
        System.out.println("4. MoMo paneer:       285");
        System.out.println("5. MoMo veg steam:    250");


        Scanner sc = new Scanner(System.in);

        int Total = 0;
        System.out.println("Enter how many orders would you like to make:");
        int n=sc.nextInt();
        System.out.println("Enter your choices: ");
        for(int i=0;i<n;i++) {
           // if(i>0)
              //  System.out.println("Enter your next choices: ");
            int Choice = sc.nextInt();
            switch (Choice) {
                case 1: {
                    System.out.println("1. MoMo veg:          150");
                    Total += 150;
                    break;
                }

                case 2: {
                    System.out.println("2. MoMo chicken:      250");
                    Total += 250;
                    break;
                }
                case 3: {
                    System.out.println("3. MoMo buff:         200");
                    Total += 200;
                    break;
                }
                case 4: {
                    System.out.println("4. MoMo paneer:       285");
                    Total += 285;
                    break;
                }
                case 5: {
                    System.out.println("5. MoMo veg steam:    250");
                    Total += 250;
                    break;
                }
                default: {
                    System.out.println("choose options from 1 to 5");
                    break;

                }
            }
        }
        System.out.println("Total Amount: "+Total);
    }
}