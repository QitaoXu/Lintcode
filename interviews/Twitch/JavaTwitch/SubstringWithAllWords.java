class TrieNode {
    
    HashMap<Character, TrieNode> children;
    boolean isWord;
    int times;
    
    public TrieNode() {
        this.children = new HashMap<Character, TrieNode>();
        this.isWord = false;
    }
}

class Trie {
    
    TrieNode root;
    
    public Trie() {
        
        this.root = new TrieNode();
    }
    
    public void insert(String word) {
        
        TrieNode node = root; 
        
        for (int i = 0; i < word.length(); i++) {
            
            char c = word.charAt(i); 
            
            if (!node.children.containsKey(c)) {
                
                node.children.put(c, new TrieNode());
            }
            
            node = node.children.get(c);
        }
        
        node.isWord = true;
    }
    
    private TrieNode find(String word) {
        
        TrieNode node = root; 
        
        for (int i = 0; i < word.length(); i++) {
            
            char c = word.charAt(i);
            
            if (!node.children.containsKey(c)) {
                return null;
            }
            
            node = node.children.get(c);
        }
        
        return node;
    }
    
    public boolean search(String word) {
        
        TrieNode node = this.find(word);
        
        return node != null && node.isWord == true;
    }
    
    public boolean startsWith(String prefix) {
        
        TrieNode node = this.find(prefix);
        
        return node != null;
    }
}

public class SubstringWithAllWords {
    public List<Integer> findSubstring(String s, String[] words) {
        
        List<Integer> results = new ArrayList<Integer>();
        
        if (s == null || s.length() == 0 || words == null || words.length == 0) 
            return results;
        
        if (s.length() < words.length * words[0].length()) {
            
            return results;
        }
        
        int wordLength = words[0].length();
        int substrLength = wordLength * words.length;
        
        Trie trie = new Trie(); 
        HashMap<String, Integer> wordsHash = new HashMap<>();
        
        for (int i = 0; i < words.length; i++) {
            
            trie.insert(words[i]);
            
            if (!wordsHash.containsKey(words[i])) {
                wordsHash.put(words[i], 0);
            }
            
            wordsHash.put(words[i], wordsHash.get(words[i]) + 1);
        }
        
        for (int i = 0; i < s.length(); i++) {
            
            if ((i + wordLength) > s.length()) break;
            
            String substring = s.substring(i, i + wordLength); 
            
            if (!trie.search(substring)) continue;
            
            HashMap<String, Integer> curtHash = new HashMap<>();
            
            for (int j = i; j < i + substrLength; j += wordLength) {
                
                if ((j + wordLength) > s.length()) break;
                
                String part = s.substring(j, j + wordLength);
                
                if (!trie.search(part)) break;
                
                if (!curtHash.containsKey(part)) {
                    curtHash.put(part, 0);
                }
                
                curtHash.put(part, curtHash.get(part) + 1);
                
                if (curtHash.equals(wordsHash)) {
                    
                    results.add(i);
                }
            }
        }
        
        return results;
    }
}