#! /usr/bin/env python
import os

class Lexicon:
    words = []
    skip = -1

    def __init__(self, filename, skip):
        self.filename = filename
        self.skip = skip

        words = [line.strip() for line in open(filename)]
        length = len(words)
        if length % skip == 0:
            length -= 1

        self.words = words
        self.length = length

    def word(self, index):
        return self.words[(self.skip * index) % self.length]


class Platypus:

    def __init__(self, *lexicons):
        self.index = 0
        self.lexicons = []
        for lex in lexicons:
            self.add_lexicon(lex)

    def add_lexicon(self, lex):
        self.lexicons.append(lex)

    def words(self):
        for index in xrange(self.length()):
            yield [lex.word(index) for lex in self.lexicons]

    def length(self):
        return reduce(lambda x, y: x.length * y.length, self.lexicons)


if __name__ == '__main__':
    nouns = Lexicon("nouns.txt", 997)
    adjectives = Lexicon("adjectives.txt", 701)
    platypus = Platypus(adjectives, nouns)

    print platypus.length()
    #for x in xrange(100):
    for x in platypus.words():
        try:
            print "%s-%s" % tuple(x)
        except IOError, e:
            exit(0)

