


class Node{
    
    Node[] links = new Node[26];
    boolean flag = false;

    void put(char ch,Node n){
        links[ch] = n;
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

    void Trie(){
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