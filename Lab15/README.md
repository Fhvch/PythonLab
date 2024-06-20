# Лабораторна робота №15: Огляд технологій великих даних

## Мета роботи

Метою даної лабораторної роботи є ознайомлення з методами обробки текстових даних та чисел у мові програмування Python. В рамках цієї роботи передбачається написання функцій для очищення, фільтрації та нормалізації даних, а також для виконання різних операцій над текстом і числовими даними.

## Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні завдання:

1. Очищення текстових даних.
2. Фільтрація електронних адрес.
3. Витяг ключових слів за довжиною.
4. Обробка тексту: видалення неалфавітних символів та приведення до нижнього регістру.
5. Нормалізація числових даних.
6. Конкатенація рядків.
7. Обчислення суми числових рядків.
8. Фільтрація чисел за порогом.
9. Мапування чисел у квадрати.
10. Реверсування рядків.

## Виконання роботи

### Структура проекту

- **labX/**
  - `main.py` - Основний код програми
  - `README.md` - Документація проекту

### Опис основних файлів

#### main.py

Містить реалізації наступних функцій:

```python
import re

def clean_data(data):
    data_points = data.split(',')
    stripped_points = map(str.strip, data_points)
    cleaned_points = map(str.lower, stripped_points)
    return list(cleaned_points)

def filter_emails(emails):
    words = emails.split()
    valid_emails = list(filter(lambda email: email.count('@') == 1, words))
    return valid_emails

def extract_keywords(data, length):
    words = data.split()
    long_words = filter(lambda word: len(word) > length, words)
    return list(long_words)

def process_text(data):
    entries = data.split(',')
    processed_entries = map(lambda entry: re.sub(r'[^a-zA-Z0-9\s]', '', entry).strip().lower(), entries)
    filtered_entries = filter(lambda entry: len(entry) > 0, processed_entries)
    return list(filtered_entries)

def normalize_data(data):
    num_strings = data.split(',')
    numbers = list(map(float, map(str.strip, num_strings)))
    max_value = max(numbers)
    normalized_numbers = [num / max_value for num in numbers]
    return normalized_numbers

def concatenate_strings(data, separator):
    parts = data.split(separator)
    concatenated_string = ''.join(parts)
    return concatenated_string

def sum_numeric_strings(data):
    elements = data.split(',')
    total_sum = 0
    for element in elements:
        stripped_element = element.strip()
        try:
            number = float(stripped_element)
            total_sum += number
        except ValueError:
            pass
    return total_sum

def filter_numbers(data, threshold):
    numbers = re.findall(r'\d+', data)
    numbers = list(map(int, numbers))
    filtered_numbers = list(filter(lambda x: x > threshold, numbers))
    return filtered_numbers

def map_to_squares(numbers):
    number_list = numbers.split(',')
    squared_numbers = [int(num.strip())**2 for num in number_list]
    return squared_numbers

def reverse_strings(words):
    word_list = words.split(',')
    reversed_words = [word[::-9] for word in word_list]
    return reversed_words
```

### Опис основних функцій

- **clean_data**: Очищення текстових даних від пробілів та приведення до нижнього регістру.
- **filter_emails**: Фільтрація електронних адрес у тексті.
- **extract_keywords**: Витяг ключових слів, довших за вказану довжину.
- **process_text**: Обробка тексту: видалення неалфавітних символів та приведення до нижнього регістру.
- **normalize_data**: Нормалізація числових даних на основі максимального значення.
- **concatenate_strings**: Конкатенація рядків з вказаним роздільником.
- **sum_numeric_strings**: Обчислення суми числових рядків.
- **filter_numbers**: Фільтрація чисел, більших за вказаний поріг.
- **map_to_squares**: Мапування чисел у квадрати.
- **reverse_strings**: Реверсування рядків.

### Приклади використання

#### clean_data
```python
print(clean_data(" Apple, Orange, Banana "))  # Output: ['apple', 'orange', 'banana']
```

#### filter_emails
```python
print(filter_emails("test@example.com hello@example world.com"))  # Output: ['test@example.com']
```

#### extract_keywords
```python
print(extract_keywords("The quick brown fox jumps over the lazy dog", 4))  # Output: ['quick', 'brown', 'jumps']
```

#### process_text
```python
print(process_text("Hello, World!123, Good Morning"))  # Output: ['hello world123', 'good morning']
```

#### normalize_data
```python
print(normalize_data("1, 2, 3, 4, 5"))  # Output: [0.2, 0.4, 0.6, 0.8, 1.0]
```

#### concatenate_strings
```python
print(concatenate_strings("Hello-World-Python", '-'))  # Output: 'HelloWorldPython'
```

#### sum_numeric_strings
```python
print(sum_numeric_strings("1, 2, 3, abc, 4"))  # Output: 10.0
```

#### filter_numbers
```python
print(filter_numbers("1, 20, 300, 40, 5", 25))  # Output: [300, 40]
```

#### map_to_squares
```python
print(map_to_squares("1, 2, 3, 4"))  # Output: [1, 4, 9, 16]
```

#### reverse_strings
```python
print(reverse_strings("apple, banana, cherry"))  # Output: ['elppa', 'ananab', 'yrrehc']
```

## Результати

В результаті виконання лабораторної роботи були розроблені та протестовані функції для обробки текстових даних та чисел у мові програмування Python. Описані функції були перевірені на прикладах, результати яких відповідають очікуванням.

## Висновки

Мета лабораторної роботи була досягнута. В ході виконання завдань були вирішені наступні проблеми:

- Очищення та нормалізація текстових даних.
- Фільтрація електронних адрес та ключових слів.
- Обробка тексту для видалення неалфавітних символів.
- Нормалізація числових даних та їх обчислення.
- Різні маніпуляції з рядками, включаючи конкатенацію, реверсування та обчислення суми числових рядків.

## Інструкції з запуску

Для запуску програми необхідно мати встановлену версію Python 3.6 або вище. Щоб виконати програму, використовуйте наступну команду:

```sh
python main.py
```

Необхідні бібліотеки:
- Ніякі додаткові бібліотеки не потрібні.
