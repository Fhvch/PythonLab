# Лабораторна робота №11: Розширена робота з масивами чисел у Python

## Мета роботи

Метою даної лабораторної роботи є ознайомлення з основними методами обробки списків та матриць у мові програмування Python. В ході роботи передбачається написання та тестування функцій для вирішення типових завдань, що стосуються маніпуляції даними у вигляді списків та матриць.

## Опис завдання

В рамках лабораторної роботи необхідно реалізувати наступні завдання:

1. Обчислення суми квадратів елементів списку.
2. Обчислення суми елементів списку, більших або рівних середньому значенню.
3. Сортування елементів списку за частотою їх появи.
4. Знаходження пропущеного числа у списку чисел від 1 до n.
5. Знаходження найдовшої послідовності послідовних чисел у списку.
6. Поворот списку на k елементів вправо.
7. Обчислення добутку всіх елементів списку, окрім поточного.
8. Знаходження максимальної суми підсписку.
9. Виведення елементів матриці по спіралі.
10. Знаходження k найближчих точок до початку координат.

## Виконання роботи

### Структура проекту

- **labX/**
  - `main.py` - Основний код програми
  - `README.md` - Документація проекту

### Опис основних файлів

#### main.py

Містить реалізації наступних функцій:

```python
def task1(numbers):
    return sum(x**2 for x in numbers)

def task2(numbers):
    avg = sum(numbers) / len(numbers)
    return sum(x for x in numbers if x >= avg)

def task3(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    sorted_numbers = sorted(numbers, key=lambda x: (-frequency[x], x))
    return sorted_numbers

def task4(numbers):
    n = len(numbers) + 1
    total_sum = n * (n + 1) // 2
    missing_number = total_sum - sum(numbers)
    return missing_number

def task5(nums):
    num_set = set(nums)
    longest_streak = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak

def task6(nums, k):
    k = k % len(nums)
    rotated_nums = nums[-k:] + nums[:-k]
    return rotated_nums

def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    for i in range(n):
        result[i] = left_products[i] * right_products[i]
    return result

def task8(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def task9(matrix):
    if not matrix:
        return []
    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result

def task10(points, k):
    distances = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
    distances.sort(key=lambda x: x[0])
    result = [point for _, point in distances[:k]]
    return result
```

### Опис основних функцій

- **task1**: Обчислює суму квадратів елементів списку.
- **task2**: Обчислює суму елементів списку, які більші або рівні середньому значенню.
- **task3**: Сортує елементи списку за частотою їх появи.
- **task4**: Знаходить пропущене число у списку чисел від 1 до n.
- **task5**: Знаходить найдовшу послідовність послідовних чисел у списку.
- **task6**: Виконує поворот списку на k елементів вправо.
- **task7**: Обчислює добуток всіх елементів списку, окрім поточного.
- **task8**: Знаходить максимальну суму підсписку.
- **task9**: Виводить елементи матриці по спіралі.
- **task10**: Знаходить k найближчих точок до початку координат.

### Приклади використання

#### task1
```python
print(task1([1, 2, 3, 4]))  # Output: 30
```

#### task2
```python
print(task2([1, 2, 3, 4]))  # Output: 7
```

#### task3
```python
print(task3([4, 4, 1, 2, 2, 2]))  # Output: [2, 2, 2, 4, 4, 1]
```

#### task4
```python
print(task4([1, 2, 4, 5, 6]))  # Output: 3
```

#### task5
```python
print(task5([100, 4, 200, 1, 3, 2]))  # Output: 4
```

#### task6
```python
print(task6([1, 2, 3, 4, 5, 6], 2))  # Output: [5, 6, 1, 2, 3, 4]
```

#### task7
```python
print(task7([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
```

#### task8
```python
print(task8([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
```

#### task9
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(task9(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

#### task10
```python
points = [(1, 3), (3, 4), (2, -1)]
print(task10(points, 2))  # Output: [(2, -1), (1, 3)]
```

## Результати

В результаті виконання лабораторної роботи були розроблені та протестовані функції для обробки списків та матриць у мові програмування Python. Описані функції були перевірені на прикладах, результати яких відповідають очікуванням.

## Висновки

Мета лабораторної роботи була досягнута. В ході виконання завдань були вирішені наступні проблеми:

- Оптимізація алгоритмів для обробки даних у списках та матрицях.
- Реалізація ефективних методів сортування та пошуку.
- Використання структур даних для зберігання та маніпуляції інформацією.

## Інструкції з запуску

Для запуску програми необхідно мати встановлену версію Python 3.6 або вище. Щоб виконати програму, використовуйте наступну команду:

```sh
python main.py
```