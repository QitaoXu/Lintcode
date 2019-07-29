import java.util.ArrayList;
import java.util.HashMap;

public class MultiDelimiter {

    public List<String> getStrings(String s, List<String> delimiters) {

        Trie trie = new Trie();

        int max = 0;

        for (String word : delimiters) {

            max = Math.max(max, word.length());

            trie.insert(word);
        }

        List<String> results = new ArrayList<String>();

        this.dfs(s, 0, trie, results, max);

        return results;
    }

    private void dfs(String s, int startIndex, Trie trie, List<String> results, int max) {

        if (startIndex == s.length()) {

            return; 
        }

        for (i = max; i >= 1; i--) {

            if ((startIndex + i) > s.length()) continue;

            String delimiter = s.substring(startIndex, startIndex + max);

            if (!trie.search(delimiter)) continue;

            results.add(s.substring(startIndex, startIndex + i));
            
            this.dfs(s, startIndex + i, trie, results, max);

        }

        this.dfs(s, startIndex + 1, trie, results, max);


    }
}

class TrieNode {

    HashMap<Character, TrieNode> children; 
    boolean isWord; 

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

        TrieNode node = this.root; 

        for (int i = 0; i < word.length(); i++) {

            if (!node.children.containsKey(word.charAt(i))) {
                node.children.put(word.charAt(i), new TrieNode());
            }

            node = node.children.get(word.charAt(i));
        }

        node.isWord = true;
    }

    private TrieNode find(String word) {

        TrieNode node = this.root; 

        for (int i = 0; i < word.length(); i++) {

            if (!node.children.containsKey(word.charAt(i))) {
                return null;
            }

            node = node.children.get(word.charAt(i));
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