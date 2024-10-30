class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    
    def insert(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children[ch] = node
            current = node
        current.is_end_of_word = True
    
    def search(self,word):
        current = self.root
        for i in word:
            node=current.children.get(i)
            if node is None:
                return False
            current=node

        if current.is_end_of_word:
            return True
        else:
            return False
        


    def delete(self, word):
        def _delete(node,word,index):
            ch = word[index]
            currentNode = node.children.get(ch)
            canThisNodeBeDeleted = False
            if currentNode is None:
                return
            if len(currentNode.children) > 1:
                _delete(currentNode, word, index+1)#لو ليها ابناء غيرك هيشغلها من هنا
                return False
            
            if index == len(word) - 1:
                if len(currentNode.children) >= 1:
                    currentNode.is_end_of_word = False
                    return False
                else:
                    node.children.pop(ch)
                    return True
            
            if currentNode.is_end_of_word == True:
                _delete(currentNode, word, index+1)
                return False

            canThisNodeBeDeleted = _delete(currentNode, word, index+1)#لو ملهاش هيشغلها من هنا
            if canThisNodeBeDeleted == True:
                node.children.pop(ch)
                return True
            else:
                return False
        _delete(self.root,word,0)


    def _collect_words(self, node):
        result = {}
        for char, child_node in node.children.items():
            result[char] = self._collect_words(child_node) 
        if node.is_end_of_word:
            result['is_end_of_word'] = True 
        else:
            result['is_end_of_word'] = False  
        return result
    
    def __str__(self):
        return str(self._collect_words(self.root))


trie = Trie()






trie.insert("apis")
trie.insert("apisu")
trie.insert("apisdrqer")

trie.delete('apisdrqer')













# trie.insert("app")
# trie.insert("api")
# trie.insert("apd")
# trie.insert("apis")
# a
# |
# ├── p
# │   ├── is_end_of_word: False
# │   ├── p
# │   │   └── is_end_of_word: True
# │   ├── i
# │   │   ├── is_end_of_word: True
# │   │   └── s
# │   │       └── is_end_of_word: True
# │   └── d
# │       └── is_end_of_word: True
# └── is_end_of_word: False



# trie.insert("wxx")
# trie.insert("txx")
# trie.insert("qxx")
# trie.insert("qxxu")
# trie.insert("dxxm")
# root
# ├── w
# │   └── x
# │       └── x (end of word)
# │       
# │   
# ├── t
# │   └── x
# │       └── x (end of word)
# │       
# │   
# │   
# │   
# ├── q
# │   └── x
# │       └── x
# │           └── u (end of word)
# │           └── (end of word)
# │       
# │   
# ├── d
# │   └── x
# │       └── x
# │           └── m (end of word)
# │           
# │       
# │   



# trie.insert("forx")
# trie.insert("gerx")
# trie.insert("forxeo")
# root
# ├── f
# │   └── o
# │       └── r
# │           └── x
# │               ├── e
# │               │   └── o (end of word)
# │               └── (end of word)
# │           
# ├── g
# │   └── e
# │       └── r
# │           └── x (end of word)



