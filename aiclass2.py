"""
Solution to second problem using letter bigrams
"""

import re, collections

def product(xs): return reduce(lambda x, y: x*y, xs)

def two_letters(text): return re.findall('..', text.lower())

def train(lett_seq):
    corp = collections.defaultdict(int)
    for n, word in enumerate(lett_seq[2:]):
        corp[(lett_seq[n], lett_seq[n+1], word)] += 1
        corp['sum'] += 1
    return corp

def prob(corpus, pair): return float((corpus[pair] + 1)) / (len(corpus) + corpus['sum'])

CORPUS = train((file('big.txt').read()))

def transpose(array):
    width = len(array[0])
    height = len(array)
    return [[array[j][i] for j in range(height)] for i in range(width)]

def strip_corr(left, right): return product(prob(CORPUS, (l[-2], l[-1], r[0])) for l, r in zip(left, right))

def combine_strips(strips): return ''.join(map(''.join, transpose(strips)))

def reorder(strips):
    closest_pair = max([(x,y) for x in strips for y in strips if x!= y], key=lambda (a, b): max(strip_corr(a, b), strip_corr(b, a)))
    c1, c2 = closest_pair
    strips.remove(c1)
    strips.remove(c2)
    correct = [c1, c2] if strip_corr(c1, c2) > strip_corr(c2, c1) else [c2, c1]
    while strips:
        left_max = max(strips, key=lambda x:strip_corr(x, correct[0]))
        right_max = max(strips, key=lambda x:strip_corr(correct[-1], x))
        if strip_corr(correct[-1], right_max) > strip_corr(left_max, correct[0]):
            q = right_max
            correct.append(q)
        else:
            q = left_max
            correct.insert(0, q)
        strips.remove(q)

    return correct

def main():
    f = open('input.txt')
    lines = [l.strip().strip('|').split('|') for l in f]
    print combine_strips(reorder(transpose(lines)))

if __name__ == '__main__':
    main()
