import java.util.*; 

public class Tuple<T, U> {

    T obj1; 
    U obj2; 

    public Tuple(T obj1, U obj2) {

        this.obj1 = obj1;
        this.obj2 = obj2;
    }

    public Tuple(T obj1) {

        this.obj1 = obj1; 
        this.obj2 = null;
    }

    public static void main(String[] args) {

        Tuple<String, Integer> tuple1 = new Tuple<String, Integer>("xqt", 23);

        
    }
}

