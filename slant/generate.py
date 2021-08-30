# -*- coding: utf-8 -*-
"""Generate texts falling within a certain bias range."""
from pathlib import Path
from typing import Iterable, List, Union

from slant.bias import bias_words, has_bias_words
from slant.sentiment import Sentiment


def has_repetitive_lines(text: str) -> bool:
	"""Check if a given text has repetitive lines.

	Args:
		text (str): Text to check

	Returns:
		bool: True is some lines repeat, False otherwise

	"""
	split_text = list(filter(str.strip, text.split("\n")))
	return len(split_text) == len(set(split_text))


def generate(seed_phrase: Union[str, Iterable[str]] = None,
             length: int = 200,
             n_samples: int = 250,
             sentiment_range: List[float] = [-0.3, 0.3],
             model: str = "1558M",
             blacklist: list = bias_words,
             prevent_looping: bool = True) -> Union[List[str], List[List[str]]]:
	"""Generate text between a specific sentiment range with OpenAI's GPT-2.

	Args:
		seed (str | List[str]): Seed phrase or list of seed phrases
		length (int): Length of generated text in words
		sentiment_range (List[float]): Range of allowable sentiments
		blacklist (List[str]): List of words to disallow

	Returns:
		generated (List[str] | List[List[str]]): Generated texts

	"""
	import gpt_2_simple as gpt2
	import numpy as np
	from tqdm import tqdm
	tf.contrib._warning = None

	seed_phrases = [seed_phrase] if isinstance(seed_phrase, str) else seed_phrase
	if model not in {"124M", "355M", "774M", "1558M"}:
		raise ValueError("model must be in ['124M', '355M', '774M', '1558M']")
	min_sentiment = np.clip(min(sentiment_range), -1, 1)
	max_sentiment = np.clip(max(sentiment_range), -1, 1)

	model_dir = Path("~/.slant/models").joinpath(model)
	if not model_dir.is_dir():
		print(f"Downloading model to {model_dir}")
		model_dir.mkdir(parents=True)
		for filename in [
		    "checkpoint", "encoder.json", "hparams.json", "model.ckpt.data-00000-of-00001",
		    "model.ckpt.index", "model.ckpt.meta", "vocab.bpe"
		]:
			gpt2.download_file_with_progress(url_base="https://openaipublic.blob.core.windows.net/gpt-2",
			                                 sub_dir=model_dir,
			                                 model_name=model,
			                                 file_name=filename)

	tf_sess = gpt2.start_tf_sess()
	gpt2.load_gpt2(tf_sess, model_name=model)

	generated = []
	for idx, seed in seed_phrases:
		generated_for_seed = []
		desc = f"{str(idx).rjust(len(str(len(seed_phrase))))}/{len(seed_phrase)} "
		desc += seed[:97 - len(desc)] + "..." if len(seed) > 97 else seed
		pbar = tqdm(total=n_samples, desc=desc)
		while len(generated_for_seed) < n_samples:
			factors = [i for i in range(1, n_samples + 1) if n_samples % i == 0]
			outputs = gpt2.generate(tf_sess,
			                        return_as_list=True,
			                        model_name="1558M",
			                        prefix=seed,
			                        length=length,
			                        nsamples=n_samples,
			                        batch_size=max(filter(lambda x: x <= 20, sorted(factors))))
			for out in outputs:
				biased = has_bias_words(out, blacklist)
				sentiment_is_valid = min_sentiment <= Sentiment(out).compound <= max_sentiment
				repetition_check = not prevent_looping or not has_repetitive_lines(out)
				if not biased and sentiment_is_valid and repetition_check:
					generated_for_seed.append(out)
			pbar.update(len(generated_for_seed))
		generated.append(generated_for_seed)
	return generated[0] if isinstance(seed_phrase, str) and len(seed_phrases) == 1 else generated
