# Лабораторна робота №11: Алгоритми роботи з числами та масивами

## Мета роботи
Навчитися реалізовувати та тестувати різноманітні алгоритми для роботи з числами та масивами.

## Опис завдання
Реалізувати функції для розв'язання наступних задач:
1. Обчислення суми квадратів чисел.
2. Обчислення суми чисел, що більші або рівні середньому значенню.
3. Сортування чисел за частотою та значенням.
4. Знаходження пропущеного числа у послідовності.
5. Знаходження найдовшої послідовності послідовних чисел.
6. Поворот масиву вправо на k позицій.
7. Обчислення масиву, де кожен елемент дорівнює добутку всіх інших елементів.
8. Знаходження максимальної суми підмасиву.
9. Згортка матриці у спіральний порядок.
10. Знаходження k найближчих точок до початку координат.

## Виконання роботи
### Структура проекту
lab11/
├── main.py
└── README.md


### Опис файлів
- `main.py`: містить всі функції для лабораторної роботи.
- `README.md`: даний файл з описом роботи та інструкціями.

### Опис основних функцій та методів
#### task1
Функція `task1` обчислює суму квадратів чисел у списку.
```python
def task1(numbers):
    return sum(x**2 for x in numbers)
```

#### task2
Функція task2 обчислює суму чисел у списку, що більші або рівні середньому значенню.
```python
def task2(numbers):
    avg = sum(numbers) / len(numbers)
    return sum(x for x in numbers if x >= avg)
```

#### task3
Функція task3 сортує числа у списку за частотою їх появи та значенням.
```python
def task3(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_numbers = sorted(numbers, key=lambda x: (-frequency[x], x))

    return sorted_numbers
```

#### task4
Функція task4 знаходить пропущене число у послідовності чисел.
```python
def task4(numbers):
    n = len(numbers) + 1
    total_sum = n * (n + 1) // 2

    missing_number = total_sum - sum(numbers)

    return missing_number
```
#### task5
Функція task5 знаходить найдовшу послідовність послідовних чисел у списку.
```python
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
```

#### task6
Функція task6 повертає масив, повернутий вправо на k позицій.
```python
def task6(nums, k):
    k = k % len(nums)

    rotated_nums = nums[-k:] + nums[:-k]

    return rotated_nums
```

#### task7
Функція task7 обчислює масив, де кожен елемент дорівнює добутку всіх інших елементів у списку.
```python
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
```

#### task8
Функція task8 знаходить максимальну суму підмасиву у списку чисел.
```python
def task8(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)

        max_sum = max(max_sum, current_sum)

    return max_sum
```

#### task9
Функція task9 згортає матрицю у спіральний порядок.
```python
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
```
#### task10
Функція task10 знаходить k найближчих точок до початку координат.
```python
def task10(points, k):
    distances = [(point[0] ** 2 + point[1] ** 2, point) for point in points]

    distances.sort(key=lambda x: x[0])

    result = [point for _, point in distances[:k]]

    return result
```
### Приклади використання
```python
print(task1([1, 2, 3]))  # Виведе: 14
print(task2([1, 2, 3, 4]))  # Виведе: 7
print(task3([4, 4, 2, 2, 2, 3]))  # Виведе: [2, 2, 2, 4, 4, 3]
print(task4([1, 2, 3, 5]))  # Виведе: 4
print(task5([100, 4, 200, 1, 3, 2]))  # Виведе: 4
print(task6([1, 2, 3, 4, 5, 6, 7], 3))  # Виведе: [5, 6, 7, 1, 2, 3, 4]
print(task7([1, 2, 3, 4]))  # Виведе: [24, 12, 8, 6]
print(task8([-2,1,-3,4,-1,2,1,-5,4]))  # Виведе: 6
print(task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Виведе: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(task10([[1, 3], [3, 4], [2, -1]], 2))  # Виведе: [[2, -1], [1, 3]]
```

### Результати
Реалізовані функції були протестовані на різних наборах даних, і всі вони виконують свої завдання коректно.

### Висновки
Мета роботи була досягнута. Було розроблено та протестовано функції для вирішення різних алгоритмічних задач. Жодних значних проблем під час розробки та тестування не виникло.

### Інструкції з запуску
- **Вимоги до середовища**: Python 3.x
- **Команда для запуску**:
1.Збережіть код у файл `main.py`.
2.Запустіть файл командою:
$ python main.py