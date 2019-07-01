import pandas as pd
from nltk.corpus import wordnet
from sys import argv

CSV_FILE = "vocab.csv"

def add_word(word,a ):
    #for consistency, the first letter is always capitalized
    try:
        word = word[0].upper() + word[1:]
    except:
        if word == "":
            return
        else:
            word = word
    syn = wordnet.synsets(word)
    #get the meaning of the word, some words are not in the word bank
    try:
        meaning = syn[0].definition()
    except:
        print("{} could not be found".format(word))
        a.write(word)
        a.write("\n")
        return
    #get the word used in context, words often to not have an example sentence
    try:
        context = syn[0].examples()[0]
    except:
        print("no exmaple sentence could be found")
        context = ''
    df = pd.read_csv(CSV_FILE)
    #commas will mess with the CSV file format
    meaning = meaning.replace(',',';')
    context = context.replace(',',';')
    data = {"Word": [word], "Meaning": [meaning], "Context": [context]}
    d = pd.DataFrame(data)
    if (df["Word"] == word).any():
        print("this word already is in the file")
        return
    else:
        a = df.append(d, ignore_index = False)
        a.to_csv(CSV_FILE, index = False)

if __name__ == "__main__":
    #the word can be an optional command line argument
    #if it not given, the program will contionusly ask for a new word
    #this is useful during study sessions etc.
    #when you might want add many words
        if len(argv) == 2:
            word = argv[1]
        else:
            while True:
                word = input("what word\n")
                add_word(word)
