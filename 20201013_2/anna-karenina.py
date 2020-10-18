from sys import stdin
from typing import Dict, Optional, List

if __name__ == '__main__':
    # Read words
    n, w = map(lambda x: int(x), input().split(','))
    words: Dict[str, int] = {}
    for line in stdin:
        start: Optional[int] = None
        for i, letter in enumerate(line):
            if letter.isalpha() and start is None:
                start = i
            if not letter.isalpha() and start is not None:
                word = line[start:i].lower()
                start = None
                if len(word) >= w:
                    words[word] = words[word] + 1 if word in words else 1

    # Find top n
    distinct_count = 0
    previous: Optional[int] = None
    output: List[str] = []
    for word, count in sorted(words.items(), key=lambda p: (p[1], p[0]), reverse=True):
        if previous == count:
            output.append(f'{count}: {word}')
        else:
            previous = count
            distinct_count += 1
            if distinct_count > n:
                break
            else:
                output.append(f'{count}: {word}')

    # Print result
    for line in reversed(output):
        print(line)
