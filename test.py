# test_tokenizer.py
from tokenizer import build_trie_from_file, tokenize

def main(text):
    # Load your dictionary
    trie = build_trie_from_file("thai_words.txt")
    
    # Tokenize
    tokens = tokenize(text, trie)
    
    print(tokens)

if __name__ == "__main__":
    i = input("Enter text to tokenize: ")
    main(i if i != "" else "ฉันไปโรงเรียนกับเพื่อน")
