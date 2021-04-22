#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author : Jean-Damien Généro
Date : 2021-04-21
Update : 2021-04-22
"""


import re


def change_keyword() -> None:
    """
    Removing year from keywords.
    :param path: path to a file
    :type path: str
    :return: none
    """
    path = input("Enter path : ")
    with open(path, 'r', encoding='utf-8') as reading:
        file = reading.read()
        file = re.sub(r'(monographie)\d{4}', r'\1', file)
        file = re.sub(r'(dirouvrage)\d{4}', r'\1', file)
        file = re.sub(r'(dirrevue)\d{4}', r'\1', file)
        file = re.sub(r'(editions)\d{4}', r'\1', file)
        file = re.sub(r'(prefpostface)\d{4}', r'\1', file)
        file = re.sub(r'(article)\d{4}', r'\1', file)
        file = re.sub(r'(chap)\d{4}', r'\1', file)
        file = re.sub(r'(artdictencyclo)\d{4}', r'\1', file)
        file = re.sub(r'(compterendu)\d{4}', r'\1', file)
        file = re.sub(r'(trad)\d{4}', r'\1', file)
        file = re.sub(r'(autre)\d{4}(, autre\w+)\d{4}', r'\1\2', file)
        file = re.sub(r'(vulgarisation)\d{4}(, vulgarisation\w+)\d{4}', r'\1\2', file)
    with open(path, 'w', encoding='utf-8') as writting:
        writting.write(file)
        print("{} ----> done !".format(path))


def make_keys() -> None:
    """
    Replacing  keys' numbers by new numbers from 1.
    """
    path = input("Enter path : ")  # path to a BibLaTeX file
    with open(path, 'r', encoding='utf-8') as reading:
        print("**** BEGINNING ANALYSING {} ****".format(path))
        file = reading.read()
        key_name_year = r"@\w+{[a-z]+[0-9]{4}"  # @entry{author2020
        # 1/ removing old keys numbers
        file = re.sub(r"(" + key_name_year + r")-\d+,", r"\1", file)
        # 2/ detecting keys
        key_plus_lines = re.findall(r"((" + key_name_year + r")(.+\n.+\n.+))", file)
        print("**** {} KEYS DETECTED ****".format(len(key_plus_lines)))
        # 3/ renumbering
        counter = 0
        for item in key_plus_lines:
            counter += 1
            print("Key n°{} : {}".format(counter, item[1]))
            new_key = item[0].replace(item[1], item[1] + "-" + str(counter))
            file = file.replace(item[0], new_key)
    with open(path, 'w', encoding='utf-8') as writting:
        writting.write(file)
        print("**** DONE ****")


make_keys()
