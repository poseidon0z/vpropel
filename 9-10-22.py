import math

word = [*input()]

sorted_word = word[:]
sorted_word.sort()

rank = 0

for word_letter in word:
    for letter in sorted_word:
        if letter != word_letter:
            value = math.factorial(len(sorted_word) - 1)
            rank += value
        else:
            sorted_word.remove(letter)
            break
rank += 1

print(rank)
