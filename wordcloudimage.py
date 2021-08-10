from wordcloud import WordCloud
import re

def splitWords(file):      
    with open(file, 'rt') as f:
        words = [word for word in f.readline().split() if word.lower() not in ['a', 'the', 'an', 'to', 'in', 'for', 'of', 'or', 'we', 'by', 'with', 'is', 'on', 'that', 'be']]
        words = [char for char in words if char.isalpha()]
    return words

def countWords(words):
    wordcount = {}
    for word in words:
        wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount

def makeImage(words):
    cloud = WordCloud()
    cloud.generate_from_frequencies(words)
    cloud.to_file("myfile.jpg")
    

if __name__ == '__main__':
    words = splitWords(r'C:\Users\cwarhus\Documents\virtualenvs\wordcloud\lorem ipsum.txt')
    wordcount = countWords(words)
    makeImage(wordcount)


