package Array;

import java.util.ArrayList;
import java.util.Arrays;

public class alternatePN {
    public static void main(String[] args) {
        int[] arr = {-1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9,0,11,12,13};
        for (int i = 0; i < arr.length-1; i++) {
            if(arr[i]>0 & arr[i+1]>0){
                for (int j = i+2; j <arr.length ; j++) {
                    if(arr[j]<0){
                        int temp = arr[i+1];
                        arr[i+1]=arr[j];
                        arr[j]=temp;
                    }
                }
        }
            if(arr[i]<0 & arr[i+1]<0){
                for (int j = i+2; j <arr.length ; j++) {
                    if(arr[j]>0){
                        int temp = arr[i+1];
                        arr[i+1]=arr[j];
                        arr[j]=temp;
                    }
                }
            }
        }
        System.out.println(Arrays.toString(arr));
        }

}
