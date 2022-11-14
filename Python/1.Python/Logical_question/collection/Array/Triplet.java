package Array;

public class Triplet {
    public static void main(String[] args) {
        int [] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int tripletSum = 13;
        for (int i = 0; i < arr.length-2; i++) {
            for (int j = i+1; j <arr.length-2 ; j++) {
                for (int k = 0; k < arr.length; k++) {
                    if(arr[i]+arr[j]+arr[k]==13){
                        System.out.println("Triplet for sum "+tripletSum+" is: {"+arr[i]+","+arr[j]+","+arr[k]+"}");
                    }

                }

            }

        }
    }
}
