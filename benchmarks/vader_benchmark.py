#-*-coding: utf-8-*-
"""Benchmark slant's VADER implementation compared to the canonical one."""
import re
from time import time
from typing import List

import slant
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# VADER's default test sentences
vader_test_sentences = [
    "VADER is smart, handsome, and funny.", "VADER is smart, handsome, and funny!",
    "VADER is very smart, handsome, and funny.", "VADER is VERY SMART, handsome, and FUNNY.",
    "VADER is VERY SMART, handsome, and FUNNY!!!",
    "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",
    "VADER is not smart, handsome, nor funny.", "The book was good.",
    "At least it isn't a horrible book.", "The book was only kind of good.",
    "The plot was good, but the characters are uncompelling and the dialog is not great.",
    "Today SUX!", "Today only kinda sux! But I'll get by, lol", "Make sure you :) or :D today!",
    "Catch utf-8 emoji such as 💘 and 💋 and 😁", "Not bad at all"
]

# 398 open web text documents, averaging 4,745 characters in length
with open("openwebtext_subset.txt", "r", encoding="utf-8") as f:
	owt_documents = [x.strip() for x in filter(str.strip, re.split(r"={20}", f.read()))]


def original_vader_time(texts: List[str]) -> float:
	"""Get execution time for the original VADER implementation.

	Args:
		texts (List[str]): Texts to score the sentiment of

	Returns:
		float: Execution time

	"""
	start_time = time()
	sentiments = []
	analyzer = SentimentIntensityAnalyzer()
	for text in texts:
		sentiments.append(analyzer.polarity_scores(text)["compound"])
	assert len(sentiments) == len(texts)
	return time() - start_time


def slant_vader_time(texts: List[str]) -> float:
	"""Get execution time for slant's VADER implementation.

	Args:
		texts (List[str]): Texts to score the sentiment of

	Returns:
		float: Execution time

	"""
	start_time = time()
	sentiments = slant.sentiment(texts).compound
	assert len(sentiments) == len(texts)
	return time() - start_time


original_vader_sentence_runtimes = []
original_vader_owt_runtimes = []
slant_vader_sentence_runtimes = []
slant_vader_owt_runtimes = []

# Run for 5 loops, clocking execution time
for _ in range(2):
	original_vader_sentence_runtimes.append(original_vader_time(vader_test_sentences))
	original_vader_owt_runtimes.append(original_vader_time(owt_documents))
	slant_vader_sentence_runtimes.append(slant_vader_time(vader_test_sentences))
	slant_vader_owt_runtimes.append(slant_vader_time(owt_documents))

mean_improvement_rate = lambda v, s: round(np.average(v) / np.average(s), 3)
max_improvement_rate = lambda v, s: round(max(v) / min(s), 3)
print("slant:VADER average sentence improvement rate =",
      mean_improvement_rate(original_vader_sentence_runtimes, slant_vader_sentence_runtimes))
print("slant:VADER average document improvement rate =",
      mean_improvement_rate(original_vader_owt_runtimes, slant_vader_owt_runtimes))
print("slant:VADER maximum sentence improvement rate =",
      max_improvement_rate(original_vader_sentence_runtimes, slant_vader_sentence_runtimes))
print("slant:VADER maximum document improvement rate =",
      max_improvement_rate(original_vader_owt_runtimes, slant_vader_owt_runtimes))
