"""
Solution to AI class Assignment using bag of words model.
"""

import re, collections

def words(text): return re.findall('[a-z]+', text.lower())

def freq_map(word_seq):
    corp = collections.defaultdict(int)
    for word in word_seq:
        corp[word] += 1
        corp['sum'] += 1
    return corp

def prob(corpus, word): return float((corpus[word] + 1)) / (len(corpus) + corpus['sum'])

CORPUS = freq_map(words(file('big.txt').read()))

def shift(word, offset): return ''.join(map(lambda c: chr(ord('a') + (ord(c) - ord('a') + offset) % 26), word))

def chance(word_seq):
    return sum(prob(CORPUS, word) for word in word_seq)

def decode(cipher):
    wlist = words(cipher)
    shifted = [[shift(word, i) for word in wlist] for i in range(26)]
    return max(shifted, key=chance)

if __name__ == '__main__':
    print ' '.join(decode('Esp qtcde nzyqpcpynp zy esp ezatn zq Lcetqtntlw Tyepwwtrpynp hld spwo le Olcexzfes Nzwwprp ty estd jplc'))
