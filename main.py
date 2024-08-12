import string
from collections import OrderedDict
import numpy as np


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text)

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

#----------- MY SOLUTION -------------->
def get_character_count(text):
    dict_keys = list(string.ascii_lowercase)
    dict_char_num = {}

    my_string = text.lower()

    for c in dict_keys:
        count_char = my_string.count(c)
        dict_char_num.update({c: count_char})
    return dict_char_num

def sort_on(dict):
    res = {key: val for key, val in sorted(dict.items(), key = lambda ele: ele[1], reverse = True)}
    return res

def print_report(text):
    num_words = get_word_count(text)
    numb_char = get_character_count(text)
    sorted_dict = sort_on(numb_char)

    keys = list(sorted_dict.keys())
    values = list(sorted_dict.values())

    
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(num_words) + " words found in the document")
    print("")
    for i in range(0,len(sorted_dict)):
        print("The " + "'" + str(keys[i]) + "'" + " character was found " + str(values[i]) + " times")
    print("--- End report ---")


main()

