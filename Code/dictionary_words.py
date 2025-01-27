import random
import sys

words_dict = '/usr/share/dict/words'
how_many_words = int(sys.argv[1])
selected_words = []

with open(words_dict, 'r') as f:
    words = f.readlines()
    for i in range(how_many_words):
        selected_words.append(random.choice(words).strip())

print(" ".join(selected_words))