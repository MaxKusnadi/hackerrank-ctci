class Trie:
    
    def __init__(self):
        root = Node("")
        self.root = root
        
    def add(self, word):
        head = None
        for x in word:
            if not head:
                head = self.root.get(x)
                if not head:
                    n = Node(x)
                    self.root.size += 1
                    self.root.child[x] = n
                    head = n
            check = head.get(x)
            head.size += 1
            if not check:
                n = Node(x)
                head.child[x] = n
                head = n
            else:
                head = check
                
    def find(self, word):
        head = None
        for x in word:
            if not head:
                head = self.root.get(x)
                if not head:
                    return 0
            check = head.get(x)
            if not check:
                return 0
            head = check
        return head.size 
                
            
class Node:
    
    def __init__(self, letter):
        self.letter = letter
        self.child = dict()
        self.size = 0
    
    def get(self, x):
        return self.child.get(x)
        
n = int(input().strip())
trie = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        trie.add(contact)
    else:
        ans = trie.find(contact)
        print(ans)

    
