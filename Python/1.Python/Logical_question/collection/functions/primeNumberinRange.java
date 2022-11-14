package functions;
import functions.Prime;
public class primeNumberinRange {
    public static void PrimeinRange(){
        for (int i = 1; i <1000 ; i++) {
            if(Prime.checkPrime(i)){
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        PrimeinRange();
    }
}
