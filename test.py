from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
text = "Go until jurong point, crazy.. Available only in bugis n great world la e buffet..."
tokens = word_tokenize(text)
print(tokens)
