# coding: utf-8

from string import ascii_lowercase


def create_cipher_columns(keyword):
    keyword = ''.join(sorted(set(keyword), key=keyword.index)).lower()
    letters = ''.join(
     letter for letter in ascii_lowercase if letter not in keyword)
    columns = [letters[i:i + 5] for i in range(0, len(letters), 5)]
    columns.insert(0, keyword)
    return columns

