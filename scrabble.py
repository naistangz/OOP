"""
Base Scrabble word calculator instructions
Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided.

Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
"""

class Scrabble:

    def score(word):
        letter_values = {"a": 1, "b": 3, "c": 3, "d": 2,
                         "e": 1, "f": 4, "g": 2, "h": 4,
                         "i": 1, "j": 8, "k": 5, "l": 1,
                         "m": 3, "n": 1, "o": 1, "p": 3,
                         "q": 10, "r": 1, "s": 1, "t": 1,
                         "u": 1, "v": 4, "w": 4, "x": 8,
                         "y": 4, "z": 10}
        total = 0
        for letter in word:
            total += letter_values[letter.lower()]
        return f"Your score is: {total}"
    player_input = input("Input your word:\n")

    print(score(player_input))

Scrabble()

