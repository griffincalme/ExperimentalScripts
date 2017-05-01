import random

list = [x for x in range(0,1000)]

print(list)

random.shuffle(list)
print(list)


def bubble_sort(unordered_list):

    is_sorted = False
    n = len(unordered_list)

    while not is_sorted:
        is_sorted=True
        for i in range(0,n-1):
            if unordered_list[i] > unordered_list[i+1]:
                is_sorted = False
                hold = unordered_list[i+1]
                unordered_list[i+1] = unordered_list[i]
                unordered_list[i] = hold
                ordered_list = unordered_list
    return ordered_list

print(bubble_sort(list))