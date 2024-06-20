import numpy as np

def interpolate_missing(numbers):
    none_indexes = [i for i, x in enumerate(numbers) if x is None]

    for index in none_indexes:
        left_neighbor = next((i for i in range(index, -1, -1) if numbers[i] is not None), None)
        right_neighbor = next((i for i in range(index, len(numbers)) if numbers[i] is not None), None)

        if left_neighbor is not None and right_neighbor is not None:
            numbers[index] = (numbers[left_neighbor] + numbers[right_neighbor]) / 2

    return numbers


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def process_batches(numbers, batch_size):
    max_values = []
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i + batch_size]
        max_values.append(max(batch))
    return max_values


def encode_string(s):
    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded


def decode_string(encoded):
    decoded = ''
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        decoded += encoded[i + 1] * count
        i += 2
    return decoded


def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


import re


def regex_search(strings, pattern):
    matched_strings = []
    regex = re.compile(pattern)
    for string in strings:
        if regex.search(string):
            matched_strings.append(string)
    return matched_strings


def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def group_by_key(data, key):
    grouped = {}
    for item in data:
        k = item[key]
        if k in grouped:
            grouped[k].append(item['value'])
        else:
            grouped[k] = [item['value']]
    return grouped

def remove_outliers(arr):
    mean = np.mean(arr)
    sd = np.std(arr)
    final_list = [x for x in arr if (x > mean - 2 * sd)]
    final_list = [x for x in final_list if (x < mean + 2 * sd)]
    return final_list
