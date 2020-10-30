class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = [None]*26
        self.wordend = 0

def search(ROOT, word, index=0):
    if not ROOT or index == len(word):
        return False
    
    i = ord(word[index])-ord('a')
    if index == len(word)-1:
        if ROOT.children[i] and ROOT.children[i].wordend > 0:
            return True
    

    return search(ROOT.children[i], word, index+1)
    
def dfs(ROOT, string=""):
    if ROOT.wordend:
        print(string)

    for i in range(26):
        if ROOT.children[i]:
            dfs(ROOT.children[i], string+ROOT.children[i].value)


def insert(ROOT, word, index=0):
    if index == len(word):
        return

    i = ord(word[index])-ord('a')

    if not ROOT.children[i]:
        ROOT.children[i] = TrieNode(word[index])
    
    ROOT.children[i].value = word[index]
    if index == len(word)-1:
        ROOT.children[i].wordend += 1

    insert(ROOT.children[i], word, index+1)

def delete(ROOT, word, index=0):
    if index == len(word):
        return
    
    i = ord(word[index])-ord('a')

    if ROOT.children[i].wordend == 1 and index == len(word)-1:
        ROOT.children[i].wordend -= 1

    delete(ROOT.children[i], word, index+1)

ROOT = TrieNode("")
words = ["abc", "abd", "abc", "xyz"]

for i in range(len(words)):
    insert(ROOT, words[i])

print(search(ROOT, "abcx"))
