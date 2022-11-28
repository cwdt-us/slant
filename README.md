[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://mit-license.org/)

<img src="./assets/images/logo.min.svg" alt="slant logo" width="250"/>

# slant
`slant` enables researchers to both reliably and efficiently assess the degree to which texts —
generated either by machines or people — contain bias. The governing concern here is the
proliferation of language generation models not being met with comparable efforts to determine the
nature of the text they produce. Due to the large scale of data they produce, analysis must be fast
and simple to encourage researcher use. The advantage of such an approach is that is as easy to run
on single, smaller examples as it is to run on large datasets. Bias is detected across multiple
dimensions, primarily race/ethnicity, gender, sexual and religious orientation, and political
affiliation and ideology.

## Installation
```bash
python3 -m pip install slant
```

## Usage
All code is self documented, further information can be found there.

### sentiment
Get the VADER sentiment score of a given text or texts.
```python
import slant

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

print(slant.sentiment(vader_test_sentences))
```

### has\_bias\_words
Determine whether a given text or texts contains potential bias words.
```python
import slant

print(slant.has_bias_words(some_text))
```

### get\_bias\_words
Return found bias words, if any, within a given text or texts.
```python
import slant

print(slant.get_bias_words(some_text))
```

### top\_words
Return the most frequently words, not including stop words, in a given text or texts.
```python
import slant

print(slant.top_words(some_text))
```

### bias\_words
`slant`'s non-exhaustive list of bias words.
```python
import slant

print(slant.bias_words)
```

### stop\_words
`slant`'s non-exhaustive list of stop words.
```python
import slant

print(slant.stop_words)
```
