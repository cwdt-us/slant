# Benchmarks

To analyze the speed of our VADER implementation vs. the canonical one, simply run 
`python3 vader_benchmark.py`

To benchmark `slant` in a consistent environment, we include a speed test in our [Colaboratory
Notebook](https://colab.research.google.com/drive/1tzkTvhg4QpgJ4GPkS1LSe7n8c5W-wAfr?usp=sharing)
and consistently see `slant` perform sentiment analysis 80x faster than the canonical VADER implementation.
