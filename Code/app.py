import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'Code'))

"""Main script, uses other modules to generate sentences."""
from flask import Flask
from dictogram import Dictogram


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    def load_corpus(filepath='Code/data/corpus.txt'):
        with open(filepath, 'r') as file:
            words = file.read().split()
        return words

    def generate_sentence(word_count):
        words = load_corpus()
        histogram = Dictogram(words)
        sentence = [histogram.sample() for _ in range(word_count)]
        return ' '.join(sentence).capitalize() + '.'
    
    return generate_sentence(50)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
