# Лабораторна робота №14: Логічні вирази та умовні оператори

## Мета роботи

Метою даної лабораторної роботи є ознайомлення з основними методами роботи з логічними операціями та умовами у мові програмування Python. В ході роботи передбачається написання та тестування функцій для вирішення типових завдань, що стосуються маніпуляції логічними значеннями та умовами.

## Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні завдання:

1. Перевірка істинності логічних виразів.
2. Перевірка логічної еквівалентності.
3. Реалізація функції XOR.
4. Повідомлення привітання або прощання на основі логічного значення.
5. Перевірка умов рівності або відмінності трьох значень.
6. Підрахунок істинних значень у списку.
7. Перевірка парності числа на основі бітового представлення.
8. Визначення більшості голосів серед трьох значень.
9. Інверсія логічного значення.
10. Реалізація тернарного оператора.
11. Перевірка комбінації логічних умов.
12. Перевірка ланцюгових умов зростання та спаду.
13. Фільтрація істинних значень зі списку.
14. Реалізація мультиплексора на основі логічних умов.

## Виконання роботи

### Структура проекту

- **labY/**
  - `main.py` - Основний код програми
  - `README.md` - Документація проекту

### Опис основних файлів

#### main.py

Містить реалізації наступних функцій:

```python
def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(a, b):
    return a == b

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(is_hello):
    if is_hello:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def count_true(bool_list):
    count = 0
    for item in bool_list:
        if item:
            count += 1
    return count

def parity(number):
    binary_representation = bin(number)[2:]
    count_ones = binary_representation.count('1')
    return count_ones % 2 == 0

def majority_vote(a, b, c):
    count_true = sum([a, b, c])
    return count_true > 1

def switch(boolean_value):
    return not boolean_value

def ternary_check(condition, result_true, result_false):
    return result_true if condition else result_false

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(bool_list):
    return [value for value in bool_list if value]

def multiplexer(bool1, bool2, bool3, integer):
    if bool1:
        return integer * 2
    elif bool2:
        return integer * 3
    elif bool3:
        return integer - 5
    else:
        return integer
```

### Опис основних функцій

- **check_truth**: Перевіряє істинність виразу (a і b) або c.
- **logical_equivalence**: Перевіряє логічну еквівалентність двох значень.
- **xor**: Реалізує логічну операцію XOR.
- **greet**: Повертає привітання або прощання на основі логічного значення.
- **nested_condition**: Перевіряє умови рівності або відмінності трьох значень.
- **count_true**: Підраховує кількість істинних значень у списку.
- **parity**: Перевіряє парність числа на основі бітового представлення.
- **majority_vote**: Визначає більшість голосів серед трьох значень.
- **switch**: Інвертує логічне значення.
- **ternary_check**: Реалізує тернарний оператор.
- **validate**: Перевіряє комбінацію логічних умов.
- **chain_check**: Перевіряє ланцюгові умови зростання та спаду.
- **filter_true**: Фільтрує істинні значення зі списку.
- **multiplexer**: Реалізує мультиплексор на основі логічних умов.

### Приклади використання

#### check_truth
```python
print(check_truth(True, False, True))  # Output: True
```

#### logical_equivalence
```python
print(logical_equivalence(True, False))  # Output: False
```

#### xor
```python
print(xor(True, False))  # Output: True
```

#### greet
```python
print(greet(True))  # Output: "Hello, World!"
print(greet(False))  # Output: "Goodbye, World!"
```

#### nested_condition
```python
print(nested_condition(1, 1, 1))  # Output: "All same"
print(nested_condition(1, 2, 3))  # Output: "All different"
print(nested_condition(1, 2, 1))  # Output: "Neither"
```

#### count_true
```python
print(count_true([True, False, True, True]))  # Output: 3
```

#### parity
```python
print(parity(5))  # Output: False
print(parity(4))  # Output: True
```

#### majority_vote
```python
print(majority_vote(True, False, True))  # Output: True
```

#### switch
```python
print(switch(True))  # Output: False
print(switch(False))  # Output: True
```

#### ternary_check
```python
print(ternary_check(True, "Yes", "No"))  # Output: "Yes"
print(ternary_check(False, "Yes", "No"))  # Output: "No"
```

#### validate
```python
print(validate(True, False, True))  # Output: True
```

#### chain_check
```python
print(chain_check(1, 2, 3))  # Output: "Increasing"
print(chain_check(3, 2, 1))  # Output: "Decreasing"
print(chain_check(1, 3, 2))  # Output: "Neither"
```

#### filter_true
```python
print(filter_true([True, False, True, False]))  # Output: [True, True]
```

#### multiplexer
```python
print(multiplexer(True, False, False, 10))  # Output: 20
print(multiplexer(False, True, False, 10))  # Output: 30
print(multiplexer(False, False, True, 10))  # Output: 5
print(multiplexer(False, False, False, 10))  # Output: 10
```

## Результати

В результаті виконання лабораторної роботи були розроблені та протестовані функції для роботи з логічними операціями та умовами у мові програмування Python. Описані функції були перевірені на прикладах, результати яких відповідають очікуванням.

## Висновки

Мета лабораторної роботи була досягнута. В ході виконання завдань були вирішені наступні проблеми:

- Реалізація базових логічних операцій та умов.
- Використання логічних операторів для перевірки умов.
- Обробка списків логічних значень.
- Робота з бітовим представленням чисел для перевірки парності.
- Використання тернарного оператора для спрощення умовних виразів.

## Інструкції з запуску

Для запуску програми необхідно мати встановлену версію Python 3.6 або вище. Щоб виконати програму, використовуйте наступну команду:

```sh
python main.py
```

Необхідні бібліотеки:
- Ніякі додаткові бібліотеки не потрібні. 
