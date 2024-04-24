from mrjob.job import MRJob
import re

class WordFrequency(MRJob):

    def mapper(self, _, line):
        word_pattern = re.compile(r'\b\w+\b')
        for word in word_pattern.findall(line):
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    WordFrequency.run()


# python word_freq.py input.txt