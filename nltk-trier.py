import nltk
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')


import nltk
text=nltk.word_tokenize("We are going out.Just you and me.")
print(nltk.pos_tag(text))