import java.util.TreeSet;
class ExamRoom {
    
    int N;
    TreeSet<Integer> students;

    public ExamRoom(int N) {
        this.N = N;
        this.students = new TreeSet<Integer>();
        
    }
    
    public int seat() {
        
        int student = 0; 
        if (this.students.size() > 0) {
            
            int dist = this.students.first();
            Integer prev = null; 
            
            for (Integer s : this.students) {
                
                if (prev != null) {
                    
                    int d = (s - prev) / 2;
                    if (d > dist) {
                        dist = d;
                        student = prev + d;
                    }
                }
                
                prev = s;
            }
            
            if (N - 1 - students.last() > dist) {
                student = N - 1;
            }
        }
        
        this.students.add(student);
        return student;
        
    }
    
    public void leave(int p) {
        
        this.students.remove(p);
        
    }
}