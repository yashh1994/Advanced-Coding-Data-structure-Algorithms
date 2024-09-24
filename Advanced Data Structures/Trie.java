class Node{
    
    Node[] links = new Node[26];
    boolean flag = false;

    void put(char ch,Node n){
        links[ch - 'a'] = n;
    }

    Node get(char ch){
        return links[ch - 'a'];
    }

    boolean isContainsKey(char ch){
        return links[ch - 'a'] != null;
    }

    void end(){
        flag = true;
    }

    boolean isEnd(){
        return flag;
    }
}

class Trie{
    private Node root;

    Trie() { // Fix: Removed 'void' to make it a proper constructor
        root = new Node();
    }
    
    void addWord(String word){
        Node node = root;
        for (int i = 0; i < word.length(); i++){
            if(!node.isContainsKey(word.charAt(i))){
                node.put(word.charAt(i), new Node());
            }
            node = node.get(word.charAt(i));
        } 
        node.end();
    }

    boolean searchWord(String word){
        Node node = root;
        for(int i = 0; i < word.length(); i++){
            if(!node.isContainsKey(word.charAt(i))){
            return false;
            }
            node = node.get(word.charAt(i));
        }
        return node.isEnd();
    }

    boolean searchPrefix(String word){
        Node node = root;
        for(int i = 0; i < word.length(); i++){
            if(!node.isContainsKey(word.charAt(i))){
                return false;
            }
            node = node.get(word.charAt(i));
        }
        return true;
    }
}


class TrieTest {
    public static void main(String[] args) {
        Trie trie = new Trie();

        // Test case 1: Add and search a word
        trie.addWord("hello");
        System.out.println(trie.searchWord("hello")); // Expected output: true

        // Test case 2: Search for a word that doesn't exist
        System.out.println(trie.searchWord("world")); // Expected output: false

        // Test case 3: Search for a prefix that exists
        System.out.println(trie.searchPrefix("hell")); // Expected output: true

        // Test case 4: Search for a prefix that doesn't exist
        System.out.println(trie.searchPrefix("heaven")); // Expected output: false

        // Test case 5: Add another word and search
        trie.addWord("world");
        System.out.println(trie.searchWord("world")); // Expected output: true

        // Test case 6: Search for a word that is a prefix of another word
        System.out.println(trie.searchWord("hell")); // Expected output: false
    }
}