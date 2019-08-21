import java.util.*;

public class PrimeProduct {

    public static void main(String[] args) {

        PrimeProduct pp = new PrimeProduct();

        int n = 80; 

        int product = 4819; 

        int[] res = pp.getProductPrime(product, pp.getPrimrNumbers(n));

        for (int number : res) {
            System.out.println(number);
        }

    }

    public int[] getProductPrime(int product, List<Integer> primeNums) {

        int start = 0, end = primeNums.size() - 1; 
        int[] res = {-1, -1};
        while (start <= end) {

            if (primeNums.get(start) * primeNums.get(end) < product) {
                start += 1;
            }

            else if (primeNums.get(start) * primeNums.get(end) > product) {
                end -= 1;
            }
            else {
                res[0] = primeNums.get(start);
                res[1] = primeNums.get(end);
                return res;
            }
        }

        return res;

    }

    public List<Integer> getPrimrNumbers (int n) {

        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true); 
        List<Integer> primeNums = new ArrayList<Integer>();

        for (int i = 2; i < n; i++) {

            if (isPrime[i] == true) {
                primeNums.add(i);
            }

            for (int j = 2; i * j < n; j++) {
                isPrime[i * j] = false;
            }
        }
        return primeNums;
    }
}