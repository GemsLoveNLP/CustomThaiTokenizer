# thai_tokenizer.py

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def longest_match(self, text, start):
        node = self.root
        match_end = -1
        i = start
        while i < len(text):
            ch = text[i]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_end:
                match_end = i
            i += 1
        return match_end

def build_trie_from_file(path_to_dict):
    trie = Trie()
    with open(path_to_dict, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()
            if word:
                trie.insert(word)
    return trie

def tokenize(text, trie):
    tokens = []
    i = 0
    while i < len(text):
        match_end = trie.longest_match(text, i)
        if match_end != -1:
            tokens.append(text[i:match_end+1])
            i = match_end + 1
        else:
            tokens.append(text[i])  # fallback: single character
            i += 1
    return tokens
