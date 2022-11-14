package functions;

import java.util.Arrays;

public class possibility {
    public static int isAllPossibilities(int[] a){
        int isAllPosibilities = 1;

        if (a.length == 0) isAllPosibilities = 0;

        for (int i = 0; i < a.length && isAllPosibilities==1; i++)

        {

            int index = -1;

            for (int j = 0; j < a.length && index==-1; j++)

            {

                if (i == a[j]) index = j;

            }

            if (index == -1)

                isAllPosibilities = 0;

        }

        return isAllPosibilities;


    }
    public static void main(String[] args) {
        int [] arr = {0,1,2,3,4,7};
        System.out.println(isAllPossibilities(arr));
        }
    }