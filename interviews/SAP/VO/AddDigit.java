import java.util.*; 

public class AddDigit {

    public static void main(String[] args) {

        AddDigit ad = new AddDigit(); 

        List<Integer> res = ad.addDigit(67);

        for (int num : res) {

            System.out.println(num);
        }
    }

    public List<Integer> addDigit(int num) {

        List<Integer> res = new ArrayList<Integer>();
        Integer n = num; 
        String ns = n.toString(); 

        for (int index = 0; index < ns.length(); index++) {

            String curt = ns.substring(0, index) + "5" + ns.substring(index);
            res.add(Integer.parseInt(curt));
        }

        res.add(Integer.parseInt(ns + "5"));

        return res;
    }

    

}