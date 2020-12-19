#!/usr/bin/env python3
"""
Consonant start finder

This module includes functions that read in an English language
dictionary and identifies unique consonant clusters that start words
"""

import re
import string


def find_consonants(dict_filename):
    """
    Find consonant clusters at the beginning of words.

    Variables:
        dict_file (required): assumed file name of list of English words
                                separated by whitespace

    Returns:
        list of unique consonant clusters that start English words
    """

    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in 'aeiouy'])
    consonant_word_starts = set()

    regex_filter = (
        f'([{consonants}]+)?'  # group 1: one or more consonants, optional
        '(.*)'  # group 2: any number of remaining characters
    )

    with open(dict_filename) as dict_file:
        # iterate over each word in dictionary
        # use re to find consonant clusters at word starts
        for word in dict_file:
            reg_match = re.match(regex_filter, word.lower().strip())

            # append to consonant_word_starts if None isn't returned for finding
            # starting consonants
            if reg_match.group(1):
                consonant_word_starts.add(reg_match.group(1))

    return sorted(consonant_word_starts)


if __name__ == '__main__':
    print(find_consonants('../inputs/words.txt'))
