# import nltk
# nltk.download()

# import module
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# taking input from the user
sentence = input("Enter the Sentence :\n")

# calculates the length of the sentence
len1 = (len(sentence))
print("Length of sentence with stopwords : {}".format(len1))

# set language
StopWords = set(stopwords.words("english"))

# The sentence is tokenized that is divided into words
words = word_tokenize(sentence)

# initializing variable to store sentence without stopwords
sentenceWithoutStopwords = []

# iterating through all the words
for w in words:
    if w not in StopWords:
        sentenceWithoutStopwords.append(w)

# joins the list
sentence_Without_Stopwords = " ".join(sentenceWithoutStopwords)

print("\nSentence without Stopwords : ")
print(sentence_Without_Stopwords)

# calculates the length of the sentence without stopwords
len2 = (len(sentence_Without_Stopwords))
print("Length of sentence without stopwords : {}".format(len2))
