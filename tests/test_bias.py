# -*- coding: utf-8 -*-
"""Test suite for bias.py"""
import slant

test_sentences = [
	"This sentence has no bias words.",
	"Karen demanded to speak to the manager again."
]

def test_bias_words_no_duplicates():
	"""Ensure no duplicates in slant.bias_words"""
	assert len(slant.bias_words) == len(set(slant.bias_words))

def test_has_bias_words_single_fail():
	"""Check if sentence with no bias words returns False"""
	assert slant.has_bias_words(test_sentences[0]) == False

def test_has_bias_words_single_success():
	"""Check if sentence with bias words returns True"""
	assert slant.has_bias_words(test_sentences[1]) == True

def test_has_bias_words_multiple():
	"""Check if multiple sentences fed in as list return correct value"""
	assert slant.has_bias_words(test_sentences) == [False, True]

def test_has_bias_words_multiple_custom_blacklist():
	assert slant.has_bias_words(test_sentences, blacklist=["no", "manager"]) == [True, True]

def test_get_bias_words_single_fail():
	"""Check if sentence with no bias words returns False"""
	assert slant.get_bias_words(test_sentences[0]) == []

def test_get_bias_words_single_success():
	"""Check if sentence with bias words returns True"""
	assert slant.get_bias_words(test_sentences[1]) == ["Karen"]

def test_get_bias_words_multiple():
	"""Check if multiple sentences fed in as list return correct value"""
	assert slant.get_bias_words(test_sentences) == [[], ["Karen"]]

def test_get_bias_words_multiple_custom_blacklist():
	assert slant.get_bias_words(test_sentences, blacklist=["no", "manager"]) == [["no"], ["manager"]]
