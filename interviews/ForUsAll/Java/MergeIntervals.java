import java.util.*;

class Interval {
      int start, end;
      Interval(int start, int end) {
           this.start = start;
           this.end = end;
      }
}

public class Solution {
    /**
     * @param intervals: interval list.
     * @return: A new interval list.
     */
    public List<Interval> merge(List<Interval> intervals) {
        // write your code here
        
        List<Interval> results = new ArrayList<Interval>();
        
        if (intervals == null || intervals.size() == 0) {
            return results;
        }
        
        intervals.sort(new Comparator<Interval>() {
            public int compare(Interval o1, Interval o2) {
                return o1.start - o2.start;
            }
        });
        
        Interval last = null; 
        
        for (Interval curt : intervals) {
            
            if (last == null || last.end < curt.start) {
                results.add(curt);
                last = curt;
            }
            
            else {
                last.end = Math.max(last.end, curt.end);
            }
        }
        
        return results;
    }
}