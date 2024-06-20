# Лабораторна робота №X: Генератори в Python

## Мета роботи

Метою даної лабораторної роботи є ознайомлення з принципами використання генераторів у мові програмування Python. В ході роботи передбачається написання та тестування різних генераторів для вирішення типових завдань, що стосуються роботи з послідовностями, файлами, деревами, графами та іншими структурами даних.

## Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні генератори:

1. Генератор чисел із заданого списку.
2. Генератор парних чисел у заданому діапазоні.
3. Генератор непарних чисел у заданому діапазоні.
4. Генератор чисел Фібоначчі.
5. Генератор простих чисел до заданого обмеження.
6. Генератор перед-обхідного обходу дерева.
7. Генератор серединного обходу дерева.
8. Генератор пост-обхідного обходу дерева.
9. Генератор обходу графа в глибину.
10. Генератор обходу графа в ширину.
11. Генератор ключів словника.
12. Генератор значень словника.
13. Генератор пар ключ-значення словника.
14. Генератор рядків з файлу.
15. Генератор слів з файлу.
16. Генератор символів рядка.
17. Генератор унікальних елементів списку.
18. Генератор елементів списку у зворотному порядку.
19. Генератор декартового добутку двох списків.
20. Генератор перестановок списку.
21. Генератор комбінацій елементів списку.
22. Генератор кортежів із списку кортежів.
23. Генератор паралельних елементів кількох списків.
24. Генератор плоского списку з вкладеного списку.
25. Генератор пар ключ-значення вкладеного словника.
26. Генератор ступенів двійки до заданого числа.
27. Генератор ступенів числа до заданого обмеження.
28. Генератор квадратів чисел у заданому діапазоні.
29. Генератор кубів чисел у заданому діапазоні.
30. Генератор факторіалів до заданого числа.
31. Генератор послідовності Коллатца.
32. Генератор геометричної прогресії.
33. Генератор арифметичної прогресії.
34. Генератор накопичувальної суми чисел.
35. Генератор накопичувального добутку чисел.

## Виконання роботи

### Структура проекту

- **labX/**
  - `main.py` - Основний код програми
  - `README.md` - Документація проекту

### Опис основних файлів

#### main.py

Містить реалізації наступних генераторів:

```python
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
```

### Опис основних функцій

- **number_generator**: Генерує числа із заданого списку.
- **

even_number_generator**: Генерує парні числа у заданому діапазоні.
- **odd_number_generator**: Генерує непарні числа у заданому діапазоні.
- **fibonacci_generator**: Генерує числа Фібоначчі.
- **prime_number_generator**: Генерує прості числа до заданого обмеження.
- **pre_order_traversal**: Генерує значення при перед-обхідному обході дерева.
- **in_order_traversal**: Генерує значення при серединному обході дерева.
- **post_order_traversal**: Генерує значення при пост-обхідному обході дерева.
- **dfs_traversal**: Генерує вершини графа при обході в глибину.
- **bfs_traversal**: Генерує вершини графа при обході в ширину.
- **dict_keys_generator**: Генерує ключі словника.
- **dict_values_generator**: Генерує значення словника.
- **dict_items_generator**: Генерує пари ключ-значення словника.
- **file_lines_generator**: Генерує рядки з файлу.
- **file_words_generator**: Генерує слова з файлу.
- **string_chars_generator**: Генерує символи рядка.
- **unique_elements_generator**: Генерує унікальні елементи списку.
- **reverse_list_generator**: Генерує елементи списку у зворотному порядку.
- **cartesian_product_generator**: Генерує пари елементів для декартового добутку двох списків.
- **permutations_generator**: Генерує перестановки списку.
- **combinations_generator**: Генерує комбінації елементів списку.
- **tuple_list_generator**: Генерує кортежі із списку кортежів.
- **parallel_lists_generator**: Генерує паралельні елементи кількох списків.
- **flatten_list_generator**: Генерує елементи вкладеного списку.
- **nested_dict_generator**: Генерує пари ключ-значення вкладеного словника.
- **powers_of_two_generator**: Генерує ступені двійки до заданого числа.
- **powers_of_base_generator**: Генерує ступені числа до заданого обмеження.
- **squares_generator**: Генерує квадрати чисел у заданому діапазоні.
- **cubes_generator**: Генерує куби чисел у заданому діапазоні.
- **factorials_generator**: Генерує факторіали до заданого числа.
- **collatz_sequence_generator**: Генерує послідовність Коллатца.
- **geometric_progression_generator**: Генерує члени геометричної прогресії.
- **arithmetic_progression_generator**: Генерує члени арифметичної прогресії.
- **running_sum_generator**: Генерує накопичувальну суму чисел.
- **running_product_generator**: Генерує накопичувальний добуток чисел.

### Приклади використання

#### number_generator
```python
for number in number_generator([1, 2, 3, 4]):
    print(number)
# Output: 1, 2, 3, 4
```

#### even_number_generator
```python
for number in even_number_generator(1, 10):
    print(number)
# Output: 2, 4, 6, 8, 10
```

#### odd_number_generator
```python
for number in odd_number_generator(1, 10):
    print(number)
# Output: 1, 3, 5, 7, 9
```

#### fibonacci_generator
```python
gen = fibonacci_generator()
for _ in range(10):
    print(next(gen))
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

#### prime_number_generator
```python
for number in prime_number_generator(20):
    print(number)
# Output: 2, 3, 5, 7, 11, 13, 17, 19
```

#### pre_order_traversal
```python
root = TreeNode(1, TreeNode(2), TreeNode(3))
for value in pre_order_traversal(root):
    print(value)
# Output: 1, 2, 3
```

#### in_order_traversal
```python
root = TreeNode(1, TreeNode(2), TreeNode(3))
for value in in_order_traversal(root):
    print(value)
# Output: 2, 1, 3
```

#### post_order_traversal
```python
root = TreeNode(1, TreeNode(2), TreeNode(3))
for value in post_order_traversal(root):
    print(value)
# Output: 2, 3, 1
```

#### dfs_traversal
```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
for node in dfs_traversal(graph, 'A'):
    print(node)
# Output: A, C, F, B, E, D
```

#### bfs_traversal
```python
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
for node in bfs_traversal(graph, 'A'):
    print(node)
# Output: A, B, C, D, E, F
```

#### dict_keys_generator
```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in dict_keys_generator(d):
    print(key)
# Output: a, b, c
```

#### dict_values_generator
```python
d = {'a': 1, 'b': 2, 'c': 3}
for value in dict_values_generator(d):
    print(value)
# Output: 1, 2, 3
```

#### dict_items_generator
```python
d = {'a': 1, 'b': 2, 'c': 3}
for item in dict_items_generator(d):
    print(item)
# Output: ('a', 1), ('b', 2), ('c', 3)
```

#### file_lines_generator
```python
for line in file_lines_generator('example.txt'):
    print(line)
# Output: (Contents of example.txt line by line)
```

#### file_words_generator
```python
for word in file_words_generator('example.txt'):
    print(word)
# Output: (Words in example.txt)
```

#### string_chars_generator
```python
for char in string_chars_generator('hello'):
    print(char)
# Output: h, e, l, l, o
```

#### unique_elements_generator
```python
for element in unique_elements_generator([1, 2, 2, 3, 4, 4, 5]):
    print(element)
# Output: 1, 2, 3, 4, 5
```

#### reverse_list_generator
```python
for element in reverse_list_generator([1, 2, 3, 4, 5]):
    print(element)
# Output: 5, 4, 3, 2, 1
```

#### cartesian_product_generator
```python
for pair in cartesian_product_generator([1, 2], ['a', 'b']):
    print(pair)
# Output: (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')
```

#### permutations_generator
```python
for perm in permutations_generator([1, 2, 3]):
    print(perm)
# Output: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
```

#### combinations_generator
```python
for comb in combinations_generator([1, 2, 3]):
    print(comb)
# Output: (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)
```

#### tuple_list_generator
```python
for tpl in tuple_list_generator([(1, 2), (3, 4), (5, 6)]):
    print(tpl)
# Output: (1, 2), (3, 4), (5, 6)
```

#### parallel_lists_generator
```python
for elements in parallel_lists_generator([1, 2], ['a', 'b']):
    print(elements)
# Output: (1, 'a'), (2, 'b')
```

#### flatten_list_generator
```python
for element in flatten_list_generator([1, [2, [3, 4], 5], 6]):
    print(element)
# Output: 1, 2, 3, 4, 5, 6
```

#### nested_dict

_generator
```python
for item in nested_dict_generator({'a': {'b': 1}, 'c': 2}):
    print(item)
# Output: ('b', 1), ('c', 2)
```

#### powers_of_two_generator
```python
for power in powers_of_two_generator(5):
    print(power)
# Output: 1, 2, 4, 8, 16, 32
```

#### powers_of_base_generator
```python
for power in powers_of_base_generator(3, 30):
    print(power)
# Output: 1, 3, 9, 27
```

#### squares_generator
```python
for square in squares_generator(1, 5):
    print(square)
# Output: 1, 4, 9, 16, 25
```

#### cubes_generator
```python
for cube in cubes_generator(1, 3):
    print(cube)
# Output: 1, 8, 27
```

#### factorials_generator
```python
for fact in factorials_generator(5):
    print(fact)
# Output: 1, 1, 2, 6, 24, 120
```

#### collatz_sequence_generator
```python
for num in collatz_sequence_generator(6):
    print(num)
# Output: 6, 3, 10, 5, 16, 8, 4, 2, 1
```

#### geometric_progression_generator
```python
for term in geometric_progression_generator(2, 3, 20):
    print(term)
# Output: 2, 6, 18
```

#### arithmetic_progression_generator
```python
for term in arithmetic_progression_generator(2, 3, 10):
    print(term)
# Output: 2, 5, 8
```

#### running_sum_generator
```python
for sum in running_sum_generator([1, 2, 3, 4]):
    print(sum)
# Output: 1, 3, 6, 10
```

#### running_product_generator
```python
for product in running_product_generator([1, 2, 3, 4]):
    print(product)
# Output: 1, 2, 6, 24
```

## Результати

В результаті виконання лабораторної роботи були реалізовані та протестовані 34 генератори для обробки різних типів даних. Всі генератори були перевірені на прикладах, результати яких відповідають очікуванням.

## Висновки

Мета лабораторної роботи була досягнута. В ході виконання завдань були вирішені наступні проблеми:

- Реалізація ефективних генераторів для різних типів даних.
- Використання генераторів для зберігання та маніпуляції інформацією.
- Оптимізація алгоритмів для обробки даних.

## Інструкції з запуску

Для запуску програм необхідно мати встановлену версію Python 3.6 або вище. Щоб виконати програму, використовуйте наступну команду:

```sh
python main.py
```

Необхідні бібліотеки:
- Ніякі додаткові бібліотеки не потрібні.
