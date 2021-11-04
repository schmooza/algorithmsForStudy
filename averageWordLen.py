# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

#https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27

import math


def average_word_len(sentenceInput):
	wordCountList = []
	averageNum = 0
	
	for p in "!?',;.$":
		sentenceInput = sentenceInput.replace(p,"")
	print("cleaned sentence >>> ", sentenceInput)
	
	
	for n in sentenceInput.split():
		letterCount = len(n)
		wordCountList.append(letterCount)
		print(wordCountList)

	for n in wordCountList:
		averageNum += n
		print(averageNum)
	lenOfString = len(sentenceInput.split())
	averageWordLenResult = averageNum / lenOfString
	print(lenOfString)
	return round(averageWordLenResult,2)

sentenceOne = "aabv. aa! aa; aa"
sentenceTwo = "b.bb bbvv$b b..bb bbvb b$$bb"

print(average_word_len(sentenceOne),"average word length in a sentence. ")
print(average_word_len(sentenceTwo),"average word length in a sentence. ")
