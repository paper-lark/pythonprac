import re


def process_match(match: re.Match):
    consonant = '[qwrtypsdfghjklzxcvbnm\']'
    vowel = '[aeiou]'
    letter = '[a-z\']'
    non_letter = '[^a-z\']'

    leading_consonants_pattern = re.compile(f'^({consonant}+)({vowel}{letter}*)', flags=re.IGNORECASE)
    one_syllable_pattern = re.compile(f'^{vowel}{consonant}*$', flags=re.IGNORECASE)
    first_vowel_pattern = re.compile(f'^({vowel}{consonant}*)({vowel}{letter}*)', flags=re.IGNORECASE)

    # prepare word
    word = match.group()
    is_capitalized = word[:1].isupper()
    result = word

    # apply rules
    leading_consonants = leading_consonants_pattern.match(word)
    one_syllable = one_syllable_pattern.match(word)
    first_vowel = first_vowel_pattern.match(word)
    if leading_consonants:
        result = leading_consonants.group(2) + leading_consonants.group(1) + 'ay'
    elif first_vowel:
        result = first_vowel.group(2) + first_vowel.group(1) + 'ay'
    elif one_syllable:
        result = word + 'yay'

    # normalize case
    result = result.lower()
    if is_capitalized:
        result = result.capitalize()
    return result


if __name__ == '__main__':
    line = input()
    while len(line) > 0:
        result = re.sub(r"[a-z']+", process_match, line, flags=re.IGNORECASE)
        print(result)
        line = input()
