import re


def split_into_words(lines):
    """Split lines into individual words and clean punctuation."""
    words = []
    for line in lines:
        words.extend(re.findall(r"[a-z0-9]+", line.lower()))
    return words
