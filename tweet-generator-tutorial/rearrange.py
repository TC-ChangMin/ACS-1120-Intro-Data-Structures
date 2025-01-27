import sys
import random

words = sys.argv[1:]
random_words_list = []

def randomize(sentence):
    sentence = list(sentence)
    random.shuffle(sentence)
    return sentence

if len(words) > 0:
    randomized_words = randomize(words)
    for word in randomized_words:
        random_words_list.append(word)
    print("Here are the randomized words:")
    print(" ".join(random_words_list))
else:
    print("No arguments provided.")