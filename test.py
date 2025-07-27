# test_tokenizer.py
from tokenizer import build_trie_from_file, tokenize

def main():
    # Load your dictionary
    trie = build_trie_from_file("thai_words.txt")
    
    # Example Thai text
    text = "ฉันไปโรงเรียนกับเพื่อน"
    
    # Tokenize
    tokens = tokenize(text, trie)
    
    print(tokens)

if __name__ == "__main__":
    main()
