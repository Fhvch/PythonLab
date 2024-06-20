from collections import deque
import itertools


def number_generator(numbers):
    for number in numbers:
        yield number


def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number


def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_number_generator(limit):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for number in range(2, limit + 1):
        if is_prime(number):
            yield number


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_order_traversal(root):
    if root is not None:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)


def in_order_traversal(root):
    if root is not None:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)


def post_order_traversal(root):
    if root is not None:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value


def dfs_traversal(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            yield node
            # Add neighbors to the stack in reverse order to maintain the correct DFS order
            stack.extend(reversed(graph[node]))


def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            yield node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


def dict_keys_generator(d):
    for key in d.keys():
        yield key


def dict_values_generator(d):
    for value in d.values():
        yield value


def dict_items_generator(d):
    for key, value in d.items():
        yield key, value


def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip('\n')


def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word


def string_chars_generator(s):
    for char in s:
        yield char


def unique_elements_generator(lst):
    seen = set()
    for element in lst:
        if element not in seen:
            seen.add(element)
            yield element


def reverse_list_generator(lst):
    for element in reversed(lst):
        yield element


def cartesian_product_generator(list1, list2):
    for element1 in list1:
        for element2 in list2:
            yield (element1, element2)


def permutations_generator(lst):
    for permutation in itertools.permutations(lst):
        yield permutation


def combinations_generator(lst):
    for r in range(1, len(lst) + 1):
        for combination in itertools.combinations(lst, r):
            yield combination


def tuple_list_generator(tuples_list):
    for tpl in tuples_list:
        yield tpl


def parallel_lists_generator(*lists):
    for elements in zip(*lists):
        yield elements


def flatten_list_generator(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list_generator(element)
        else:
            yield element


def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)


def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i


def powers_of_base_generator(base, limit):
    power = 0
    result = 1
    while result <= limit:
        yield result
        power += 1
        result = base ** power


def squares_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 2


def cubes_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 3


def factorials_generator(n):
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    for number in range(n + 1):
        yield factorial(number)


def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n


def geometric_progression_generator(initial, ratio, limit):
    term = initial
    while term <= limit:
        yield term
        term *= ratio


def arithmetic_progression_generator(initial, difference, limit):
    current = initial
    while current <= limit:
        yield current
        current += difference


def running_sum_generator(numbers):
    running_sum = 0
    for number in numbers:
        running_sum += number
        yield running_sum


def running_product_generator(numbers):
    running_product = 1
    for number in numbers:
        running_product *= number
        yield running_product
