def can_spell(letters, word):
    # reverse sort to get the blanks ('?') to the end of letters string,
    # so that the greedy algorithm works
    letters = sorted(letters, reverse=True)
    word = list(word)

    for letter in letters:
        if len(word) == 0:
            return True
        elif letter == '?':
            word.pop()
        elif letter in word:
            word.remove(letter)

    return len(word) == 0