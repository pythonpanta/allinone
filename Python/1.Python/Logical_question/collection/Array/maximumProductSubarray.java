package Array;

import java.util.ArrayList;

public class maximumProductSubarray {
    public static void main(String[] args) {
        int[] arr = {3, 5, 6, 9, -1, 8, 0, 1};
        int product=1;
        ArrayList<Integer> Products = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            product*=arr[i];
            Products.add(product);
        }
            int maxProduct = 0;
        for (int i = 0; i < Products.size(); i++) {
            if(maxProduct<Products.get(i)){
                maxProduct=Products.get(i);
            }
        }
        System.out.println("maximum Product of sub Array: "+maxProduct);
    }
}
