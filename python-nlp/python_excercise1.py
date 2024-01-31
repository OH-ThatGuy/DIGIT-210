# start with project text file. Pull its tagged words. Also pull its whole text.
# objective: Learn to open and read in data from files.
# play with spaCy
# If necessary at Git Bash or terminal do: pip3 install spacy

import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

zuckGPT = open('chatgpt_zuck.txt', 'r', encoding='utf8')
words = zuckGPT.read()
wordstrings = str(words)
print(wordstrings)

# count=0
# for w in words:
#     count += 1
#     print(count, ": ", w)

# start playing with spaCy and nlp:
zuckWords = nlp(wordstrings)
for token in zuckWords:
    # if token.pos_ == "VERB":
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)

# On windows ctrl / comments out blocks.
# On mac command / comments out blocks
# grimmFile = open('grimm.txt', 'r')
# doc2 = grimmFile.read()
# docstring = str(doc2)
# print(doc2)
