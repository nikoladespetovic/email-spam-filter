import os
from collections import Counter
import pickle as c
from sklearn import *

def load(clf_file):
    with open(clf_file, 'rb') as fp:
        clf = c.load(fp)
    return clf

def make_dict():
    direc = "emails/"
    files = os.listdir(direc)

    emails = [direc + email for email in files]

    words = []
    c = len(emails)
    for email in emails:
        f = open(email, encoding="utf8", errors='ignore')
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)

clf = load("text-classifier.mdl")
d = make_dict()

# features = []
# input_string = input(">")

# for word in d:
#     features.append(input_string.count(word[0]))

# res = clf.predict([features])

# print(["Not Spam", "Spam!"][res[0]])

while True:
    features = []
    inp = input(">")
    if inp == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print(["Not Spam", "Spam!"][res[0]])
