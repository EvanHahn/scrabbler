#!/usr/bin/env python3
from sys import argv
from can_spell import can_spell

def main(argv):
    letters = argv[1]

    result = []
    with open('dictionary.txt', 'r') as words_file:
        for line in words_file:
            word = line.strip()
            if can_spell(letters, word):
                result.append(word)

    result = sorted(result, key=lambda w: len(w), reverse=True)

    for word in result:
        print(word)

if __name__ == '__main__':
    main(argv)
