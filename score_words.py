def count_vowels(word):
    vowels = 'aeiouy'
    return sum(letter in vowels for letter in word)


def score_words(words):
    score = 0
    for word in words:
        if count_vowels(word) % 2 == 0:
            score += 2
        else:
            score += 1
    return score


if __name__ == '__main__':
    n = int(input())
    words = input().split()
    print(score_words(words))