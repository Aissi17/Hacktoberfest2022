import math


def binary_search(array, start, finish, to_find):
    print(array, start, finish)
    if start > finish:
        return "Not Found"

    middle = math.floor((start+finish)/2)
    if array[middle] > to_find:
        return binary_search(array, start, middle - 1, to_find)
    elif array[middle] < to_find:
        return binary_search(array, middle + 1, finish, to_find)
    else:
        return middle
    

def bubble_sort(array):
    for i in range(len(array)):
        print(array)
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                array[j - 1], array[j] = array[j], array[j - 1]

    return array

def counting_sort(array, k):
    c = [0] * k
    result = [0] * len(array)
    print('Original Array: ', array)

    for value in array:
        c[value-1] += 1

    print('-----')
    print('c after counting: ', c)
    print('-----')

    for i in range(1, k):
        c[i] += c[i-1]

    print('c after previous elements: ', c)
    print('-----')
    for i in range(len(array), 0, -1):
        value = array[i-1]
        index = c[value - 1] - 1
        result[index] = value
        print('result: ', result)

    return result

def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        print(array)

    return array

def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array.pop(0)
    left = []
    right = []

    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    array = quick_sort(left) + [pivot] + quick_sort(right)
    print(array)
    return array