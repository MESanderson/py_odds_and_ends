import urllib.request
from bs4 import BeautifulSoup
from collections import Counter
from itertools import zip_longest, tee, islice
import re

def retrieve_page():
    """
    Function to access webpage and scrape body of text
    """

    with urllib.request.urlopen(r'https://en.wikipedia.org/wiki/Machine_learning') as f:
        dat = f.read().decode('utf8')

    soup = BeautifulSoup(dat, "lxml")
    return soup.find(id='bodyContent').getText()


def split_words(text):
    """
    Simple function to lower case a block of text and split it into words (on spaces).

    :param text: string of text
    :return: generator of lower case words
    """
    return (x.lower() for x in text.split())


def get_word_count(word_list):
    """
    Real simple wrapper around Counter object. Probably overkill
    :param word_list: iter of cleaned words to count ([string])
    :return: collections.Counter object
    """
    return Counter(word_list)


def remove_numbers_symbols(text_iter):
    """
    Cleaning generator to remove anything that isn't a letter
    :param text_iter: input iter of strings ([string])
    :return: generator of words with non alphabet charcters removed
    """
    for word in text_iter:
        yield re.sub('[^a-zA-Z]', '', word)


def remove_empty_words(text_iter):
    """
    Generator for removing 'empty' words. Could probably have just used filter from itertools
    :param text_iter: input iter of strings ([string])
    :return: generator of non empty strings
    """
    return (x for x in text_iter if x != '')


def remove_small_words(text_iter):
    """
    Function to remove mostly prepositions.
    :param text_iter: iter of strings ([string])
    :return: generator of words with small words removed.
    """
    SMALL_WORDS = {'a', 'the', 'an', 'and', 'on', 'it', 'but', 'for', 'of', 'to', 'in', 'is', 'that',
                   'are', 'as', 'with', 'by', 'be', 'or', 'also', 'has', 'its', 'between', 'this'}
    return (x for x in text_iter if x not in SMALL_WORDS)


def print_most_common_words(text, num_most_common=10):
    text_split = split_words(text)
    text_gen = remove_small_words(remove_empty_words(remove_numbers_symbols(text_split)))

    text_hist = get_word_count(text_gen)
    for k in text_hist.most_common(num_most_common):
        print(k)


def print_most_common_word_grouping(text, num_words=2, num_most_common=10):
    text_split = split_words(text)
    text_clean = remove_small_words(remove_empty_words(remove_numbers_symbols(text_split)))
    word_iters = tee(text_clean, num_words)

    for i, x in enumerate(word_iters):
        [next(x) for x in word_iters[:i]]

    tup_gen = (ktuple[::-1] for ktuple in zip_longest(*word_iters))

    c=Counter(tup_gen)

    for k in c.most_common(num_most_common):
        print(k)



text = retrieve_page()
print_most_common_words(text)
print_most_common_word_grouping(text,2)
print("Hello World")
