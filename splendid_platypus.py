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

    def __iter__(self):
        return self

    def next(self):
        ret = []
        for lex in self.lexicons:
            ret.append(lex.word(self.index))

        self.index +=1
        return ret


if __name__ == '__main__':
    nouns = Lexicon("nouns.txt", 997)
    adjectives = Lexicon("adjectives.txt", 701)
    platypus = Platypus(adjectives, nouns)

    for x in range(10000):
      print "%s-%s" % tuple(platypus.next())

