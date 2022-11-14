package Array;

public class maxnumfromarray {
    static void bubbleSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 1; j < arr.length - i; j++) {
                if (arr[j - 1] < arr[j]) {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;
                }
            }
        }
    }
        public static void main(String[] args) {
        int[] arr = {1, 2, 3, 0, 4, 6};
        int maxNum = 0;
        bubbleSort(arr);
        for (int i=0;i<arr.length;i++){
            maxNum=maxNum*10+arr[i];
        }
        System.out.println("Maximum possible number: "+maxNum);
    }
}
