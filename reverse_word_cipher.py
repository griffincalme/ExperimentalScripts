#!/usr/bin/python3

dictionary_file = open("/usr/share/dict/words")
dictionary = dictionary_file.read().splitlines()

secret = 'ELPPAEIPSIDOOG'

secret = secret.lower()
rev = secret[::-1]


def string_slice(s):
    length = len(s)
    for size in range(1, length + 1):
        for start in range(0, (length - size) + 1):
            yield s[start:start+size]

word_list = []
for my_slice in string_slice(rev):
    for line in dictionary:
        if my_slice == line:

            word_list.append(my_slice)

word_list.reverse()
print(word_list)
