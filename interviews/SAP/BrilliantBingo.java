import java.util.*; 

public class BrilliantBingo {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in); 
        int num = sc.nextInt();
        sc.close();

        BrilliantBingo bb = new BrilliantBingo();

        System.out.println(bb.getMinNumToWin(num));
    }

    public int getMinNumToWin(int num) {

        HashSet<Integer> set = new HashSet<Integer>(); 

        int round = 0; 
        
        while (set.size() != 10) {

            round += 1;

            int curtNum = num * round; 

            while (curtNum > 0) {

                int digit = curtNum % 10; 

                set.add(digit);

                curtNum = curtNum / 10;
            }

        }

        return round;
    }
}