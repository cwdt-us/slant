# -*- coding: utf-8 -*-
"""Test suite for bias.py"""
import slant
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

vader_test_sentences = [
	"VADER is smart, handsome, and funny.",
	"VADER is smart, handsome, and funny!",
	"VADER is very smart, handsome, and funny.",
	"VADER is VERY SMART, handsome, and FUNNY.",
	"VADER is VERY SMART, handsome, and FUNNY!!!",
	"VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",
	"VADER is not smart, handsome, nor funny.",
	"The book was good.",
	"At least it isn't a horrible book.",
	"The book was only kind of good.",
	"The plot was good, but the characters are uncompelling and the dialog is not great.",
	"Today SUX!",
	"Today only kinda sux! But I'll get by, lol",
	"Make sure you :) or :D today!",
	"Catch utf-8 emoji such as 💘 and 💋 and 😁",
	"Not bad at all"
]


def test_vader_compound():
	"""Ensure no duplicates in slant.bias_words"""
	vader_sentiments = []
	analyzer = SentimentIntensityAnalyzer()
	for sentence in vader_test_sentences:
		vader_sentiments.append(analyzer.polarity_scores(sentence)["compound"])
	assert vader_sentiments == slant.sentiment(vader_test_sentences).compound

def test_vader_neg():
	"""Ensure no duplicates in slant.bias_words"""
	vader_sentiments = []
	analyzer = SentimentIntensityAnalyzer()
	for sentence in vader_test_sentences:
		vader_sentiments.append(analyzer.polarity_scores(sentence)["neg"])
	assert vader_sentiments == slant.sentiment(vader_test_sentences).neg


def test_vader_neu():
	"""Ensure no duplicates in slant.bias_words"""
	vader_sentiments = []
	analyzer = SentimentIntensityAnalyzer()
	for sentence in vader_test_sentences:
		vader_sentiments.append(analyzer.polarity_scores(sentence)["neu"])
	assert vader_sentiments == slant.sentiment(vader_test_sentences).neu

def test_vader_pos():
	"""Ensure no duplicates in slant.bias_words"""
	vader_sentiments = []
	analyzer = SentimentIntensityAnalyzer()
	for sentence in vader_test_sentences:
		vader_sentiments.append(analyzer.polarity_scores(sentence)["pos"])
	assert vader_sentiments == slant.sentiment(vader_test_sentences).pos
