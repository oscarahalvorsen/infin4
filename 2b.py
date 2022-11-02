import codecs
import os
import string


def simpleTextIndexer(directory: string, stopWordsFile: string):
    stopWords = codecs.open(stopWordsFile, "r", "utf-8").read()
    wordDict = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        doc = codecs.open(f, "r", "utf-8").read().lower()
        wordList=doc.translate(str.maketrans('','',string.punctuation+"\n\r\t")).split()
        wordList = [word for word in wordList if word not in stopWords]
        for word in wordList:
            if word not in wordDict:
                wordDict[word] = {filename: 1}
            elif filename not in wordDict[word]:
                wordDict[word][filename] = 1
            else:
                wordDict[word][filename] += 1
    return {key: value for key, value in sorted(wordDict.items())}

directory = "data_assignment"
stopWordsFile ="stopwords.txt"

print(simpleTextIndexer(directory, stopWordsFile))
