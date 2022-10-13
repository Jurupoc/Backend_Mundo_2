import num2words
import re
import string
from decimal import DecimalException

import nltk
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from unidecode import unidecode

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


def get_tags(text) :
    # processamento básico
    text = text.lower()
    text = unidecode(text)
    text = re.sub(',|\.|/|$|\(|\)|-|\+|:|•', '', text)

    # Remove espaços
    text = re.sub('\s+', ' ', text)
    # remove remanescentes
    text = ' '.join([word for word in word_tokenize(text) if not ( len(word)<2 and not word.isdigit() or "'" in word and len(word)<4)])

    # remove simbolos
    symbols = string.punctuation
    for s in symbols:
        text = text.replace(s,'')

    # substituindo números por dígitos
    text_temp = word_tokenize(text)
    for index, word in enumerate(text_temp):
        try:
            if word.isnumeric():
                text_temp[index] = num2words.num2words(word)
        except (ValueError, DecimalException):
            text_temp[index] = ''
            continue
    text = ' '.join(text_temp)

    #Aplicando o lemmatizer
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text)])

    #Aplicando o Stemmer
    stemmer = SnowballStemmer('portuguese')
    text = ' '.join([stemmer.stem(word) for word in word_tokenize(text)])

    return text