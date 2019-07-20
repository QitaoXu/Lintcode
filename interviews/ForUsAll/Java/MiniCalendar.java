import java.util;
import java.util.ArrayList;
import java.util.TreeSet;
import java.util.Iterator;

public class MiniCalendar {
    public static void main(String[] args) {

        Calendar calendar = new Calendar(); 

        ArrayList<Boolean> results = new ArrayList<>();

        results.add(calendar.add(1, 2)); 
        results.add(calendar.add(5, 7));
        results.add(calendar.add(3, 4));
        results.add(calendar.add(3, 4));
        results.add(calendar.add(5, 6)); 
        results.add(calendar.cancel(1, 2));

        System.out.println(results);

    }
}

class Event implements Comparable<Event> {

    int start;
    int end;

    public Event(int start, int end) {
        this.start = start;
        this.end = end;
    }

    public boolean isOverlapPrev(Event other) {

        if (other == null) {
            return false;
        }

        if (this.start < other.end) {
            return true;
        }

        return false;
    }

    public boolean isOverlapNext(Event other) {

        if (other == null) {
            return false;
        }

        if (this.end > other.start) {
            return true;
        }

        return false;
    }
 
    @Override
    public int compareTo(Event other) {

        if (this.start == other.start) {

            return this.end - other.end;
        }

        return this.start - other.start;
    }
}

class Calendar{

    TreeSet<Event> events; 

    public Calendar() {

        this.events = new TreeSet();
    }

    public boolean add(int start, int end) {

        if (end >= start) {
            return false;
        }

        Event e = new Event(start, end);

        if (this.events.contains(e)) {
            return false;
        }

        this.events.add(e); 

        Event prev = this.events.lower(e);
        Event next = this.events.higher(e); 

        if (e.isOverlapPrev(prev) == true || e.isOverlapNext(next) == true) {
            
            this.events.remove(e);
            // System.out.println(e.start + "Overlap");
            return false;
        }

        return true;
    }

    public boolean cancel(int start, int end) {

        if (end >= start) {
            return false;
        }

        Event e = new Event(start, end); 

        if (this.events.contains(e)) {

            this.events.remove(e);
            return true;
        }
        else {
            return false;
        }
    }


}