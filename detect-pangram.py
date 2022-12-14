# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether it is a pangram. Return True if it is,
# False if not. Ignore numbers and punctuation.

def is_pangram(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for chars in s:
        if chars not in letters:
            return 'false'
        else:
            return 'true'

print(is_pangram('abccdefghijklmnopqrstuvwxyz'))