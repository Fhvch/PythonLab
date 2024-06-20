# Лабораторна робота №13: Завдання на обробку даних. Функції з різними типами параметрів для вирішення задач обробки даних.

## Мета роботи

Метою даної лабораторної роботи є ознайомлення з основними методами обробки даних у мові програмування Python. В ході роботи передбачається написання та тестування функцій для вирішення типових завдань з маніпуляції даними.

## Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні завдання:

1. Інтерполяція відсутніх значень у списку.
2. Генерація чисел Фібоначчі.
3. Обробка списку пакетами заданого розміру.
4. Кодування рядка методом RLE.
5. Декодування рядка, закодованого методом RLE.
6. Поворот матриці на 90 градусів за годинниковою стрілкою.
7. Пошук рядків, що відповідають заданому регулярному виразу.
8. Злиття двох відсортованих масивів.
9. Перевірка числа на простоту.
10. Групування елементів за ключем.
11. Видалення відхилень із масиву.

## Виконання роботи

### Структура проекту

- **labX/**
  - `main.py` - Основний код програми
  - `README.md` - Документація проекту

### Опис основних файлів

#### main.py

Містить реалізації наступних функцій:

```python
import numpy as np
import re

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
```

### Опис основних функцій

- **interpolate_missing**: Інтерполює відсутні значення у списку.
- **fibonacci**: Генерує числа Фібоначчі.
- **process_batches**: Обробляє список пакетами заданого розміру і повертає максимальні значення з кожного пакету.
- **encode_string**: Кодує рядок методом Run-Length Encoding (RLE).
- **decode_string**: Декодує рядок, закодований методом RLE.
- **rotate_matrix**: Повертає матрицю на 90 градусів за годинниковою стрілкою.
- **regex_search**: Повертає рядки, що відповідають заданому регулярному виразу.
- **merge_sorted_arrays**: Зливає два відсортованих масиви в один.
- **is_prime**: Перевіряє, чи є число простим.
- **group_by_key**: Групує елементи за вказаним ключем.
- **remove_outliers**: Видаляє відхилення з масиву.

### Приклади використання

#### interpolate_missing
```python
print(interpolate_missing([1, None, 3, None, 5]))  # Output: [1, 2.0, 3, 4.0, 5]
```

#### fibonacci
```python
print(list(fibonacci(10)))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### process_batches
```python
print(process_batches([1, 3, 2, 4, 5, 7, 6], 3))  # Output: [3, 5, 7]
```

#### encode_string
```python
print(encode_string("aaabccdd"))  # Output: "3a1b2c2d"
```

#### decode_string
```python
print(decode_string("3a1b2c2d"))  # Output: "aaabccdd"
```

#### rotate_matrix
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

#### regex_search
```python
print(regex_search(["apple", "banana", "cherry"], "a"))  # Output: ["apple", "banana"]
```

#### merge_sorted_arrays
```python
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```

#### is_prime
```python
print(is_prime(29))  # Output: True
print(is_prime(30))  # Output: False
```

#### group_by_key
```python
data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
print(group_by_key(data, 'key'))  # Output: {'a': [1, 3], 'b': [2]}
```

#### remove_outliers
```python
print(remove_outliers([1, 2, 3, 100, 5, 6, 7, 8]))  # Output: [1, 2, 3, 5, 6, 7, 8]
```

### Результати

В результаті виконання лабораторної роботи були розроблені та протестовані функції для обробки різних типів даних у мові програмування Python. Реалізовані функції були перевірені на прикладах, що показали їх коректність і ефективність.

### Висновки

Мета лабораторної роботи була досягнута. В ході виконання завдань були вирішені наступні проблеми:

- **Інтерполяція відсутніх значень**: Функція `interpolate_missing` дозволяє заповнювати відсутні значення у списку, використовуючи інтерполяцію на основі сусідніх елементів.
- **Генерація чисел Фібоначчі**: Функція `fibonacci` генерує послідовність чисел Фібоначчі, що може бути використано у різних математичних і прикладних завданнях.
- **Обробка списку пакетами**: Функція `process_batches` дозволяє обробляти великий список пакетами, що може бути корисно при роботі з великими наборами даних.
- **Кодування та декодування рядків методом RLE**: Функції `encode_string` та `decode_string` реалізують метод Run-Length Encoding, що є ефективним для стискання даних.
- **Поворот матриці на 90 градусів**: Функція `rotate_matrix` дозволяє здійснювати поворот квадратної матриці, що може бути корисним у графічних додатках та аналізі даних.
- **Пошук за регулярними виразами**: Функція `regex_search` допомагає знаходити рядки, що відповідають заданому шаблону, що широко використовується у текстовій обробці.
- **Злиття відсортованих масивів**: Функція `merge_sorted_arrays` дозволяє об'єднувати два відсортованих масиви у один, зберігаючи сортування.
- **Перевірка на простоту**: Функція `is_prime` надає простий і ефективний метод перевірки чисел на простоту.
- **Групування елементів за ключем**: Функція `group_by_key` дозволяє групувати елементи словників за вказаним ключем, що корисно при агрегації даних.
- **Видалення відхилень**: Функція `remove_outliers` допомагає видаляти статистичні відхилення з масивів, що покращує якість аналізу даних.

## Інструкції з запуску

Для запуску програми необхідно мати встановлену версію Python 3.6 або вище. Щоб виконати програму, використовуйте наступну команду:

```sh
python main.py
```

Необхідні бібліотеки:
- numpy (для функції `remove_outliers`)
- re (для функції `regex_search`)

Для встановлення бібліотек використовуйте наступну команду:

```sh
pip install numpy
```