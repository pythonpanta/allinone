package loop;

import java.util.HashMap;
import java.util.Scanner;

public class frequency {
    public static void main(String[] args) {
        HashMap<String,Integer> frequency = new HashMap<>();
        int count = 0;
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        while(num!=0){
            int rem = num%10;
            num/=10;
            switch (rem){
                case 1:
                    if(frequency.containsKey("One"))
                        frequency.replace("One",frequency.get("One")+1);
                    else
                        frequency.put("One",1);
                    break;
                case 2:
                    if(frequency.containsKey("Two"))
                        frequency.replace("Two",frequency.get("Two")+1);

                    else
                        frequency.put("Two",1);
                    break;
                case 3:
                    if(frequency.containsKey("Three"))
                        frequency.replace("Three",frequency.get("Three")+1);
                    else
                        frequency.put("Three",1);
                    break;
                case 4:
                    if(frequency.containsKey("Four"))
                        frequency.replace("Four",frequency.get("Four")+1);
                    else
                        frequency.put("Four",1);
                    break;
                case 5:
                    if(frequency.containsKey("Five"))
                        frequency.replace("Five",frequency.get("Five")+1);
                    else
                        frequency.put("Five",1);
                    break;
                case 6:
                    if(frequency.containsKey("Six"))
                        frequency.replace("Six",frequency.get("Six")+1);
                    else
                        frequency.put("Six",1);
                    break;

                case 7:
                    if(frequency.containsKey("Seven"))
                        frequency.replace("Seven",frequency.get("Seven")+1);
                    else
                        frequency.put("Seven",1);
                    break;

                case 8:
                    if(frequency.containsKey("Eight"))
                        frequency.replace("Eight",frequency.get("Eight")+1);
                    else
                        frequency.put("Eight",1);
                    break;

                case 9:
                    if(frequency.containsKey("nine"))
                        frequency.replace("Nine",frequency.get("Nine")+1);
                    else
                        frequency.put("Nine",1);
                    break;

                case 0:
                    if(frequency.containsKey("Zero"))
                        frequency.replace("Zero",frequency.get("Zero")+1);
                    else
                        frequency.put("Zero",1);
                    break;
                default:
                    System.out.println("Doesn't feel like a Number:");
                    break;


            }
        }
        System.out.print("Frequency of digits in a Number are: ");
        System.out.println(frequency);
    }
}
