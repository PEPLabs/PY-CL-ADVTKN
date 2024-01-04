"""
Advanced Tokenization

Earlier, we explored techniques for pre-processing the text prior to the analysis. The techniques involved removing punctuations, removing stopwords, and word and sentence tokenization. In this module we continue to explore more advanced text processing techniques that will help the model understand the natural language better.
"""


"""
Stemming
Stemming is a text processing technique where we reduce words to their root form. For example, words "learning" and "learner" would both be reduced to the root word "learn". Stemming allows us to focus on the core meaning of the word instead of being distracted by different ways in which they are being used. It is important to note that the words that they get reduced to may not be dictionary words and is less precise than lemmatization. However, stemming is computationally efficient and useful in scenarios where speed is crucial.
"""

"""
NLTK provides a snowball stemmer which we'll be using here
"""
from nltk.stem.snowball import EnglishStemmer
from nltk.tokenize import word_tokenize

def sampleStemming():
    text = "The artist decided to create a new painting. Creating art is a form of self-expression. She hoped to create an atmosphere of creativity in her studio where she could freely create. The act of creation brought her joy, and she believed that anyone could create something beautiful with a bit of inspiration."

    words = word_tokenize(text)
    print(words)
    stemmer = EnglishStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    print(stemmed_words)


def stemmingExercise():
    return 

"""
Lemmatizing 
Coming from the word "lemma", lemmatizing is finding the lemma of a word. Lemma in linguistics is the basic form of a word. For example, the word "be" would be the lemma for words like "is", "am", "are", "was", etc. This is how dictionaries organize the words, by the words' lemma.
This technique yields more sophisticated and consistent result than stemming. Lemmatization can help in improving the accuracy of the text analysis and reducing the data size, as it reduces the variation a word can take. However, it is slower than stemming and it can lead to ambiguity since does not know the context in which the word is used.
"""
