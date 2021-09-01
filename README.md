[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

<img src="./images/logo.min.svg" alt="slant logo" width="250"/>

# slant
`slant` enables researchers to both reliably and efficiently generate text falling within a
predetermined sentiment range using GPT-2. Outside of fast, sentiment-bounded text generation,
`slant` provides a simple interface to our implementation of Hutto and Gilbert's VADER algorithm, 
which produces identical results up to 70x faster. Finally, `slant` includes a dictionary of
potentially biasing words, against which it checks generated text against, while also recognizing
combinations of adjectives and proper nouns for researchers to manually verify, helping to minimize
the possibility of generating text incongruous with commonly-known fact.

`slant` was designed to be used by researchers who create and implement text-based survey
experiments, particularly those that rely on vignettes. We expect that it will be particularly
useful to researchers doing work in substantive areas where the bias contained and perpetuated by
GPT-2 is most problematic, such as in race and ethnic politics.

## Usage
All code is self documented, further information can be found there.
### Sentiment
Get the VADER sentiment score of a given text or texts.
```python
from slant import Sentiment

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

print(Sentiment(text).compound)
```

### has\_bias\_words
Determine whether a given text or texts contains potential bias words.
```python
from slant import has_bias_words

print(has_bias_words(some_text))
```

### get\_bias\_words
Return found bias words, if any, within a given text or texts.
```python
from slant import get_bias_words

print(get_bias_words(some_text))
```

### top\_words
Return the most frequently words, not including stop words, in a given text or texts.
```python
from slant import top_words

print(top_words(some_text))
```

### bias\_words
`slant`'s non-exhaustive list of bias words.
```python
from slant import bias_words

print(bias_words)
```

### stop\_words
`slant`'s non-exhaustive list of stop words.
```python
from slant import stop_words

print(stop_words)
```
