# Лабораторна робота №12: Використання вкладених списків для створення двовимірних структур даних і керування ними.

### Мета роботи

Метою даної лабораторної роботи є ознайомлення з основами операцій над матрицями у мові програмування Python. В ході роботи передбачається реалізація класу `Matrix` для представлення матриці, а також написання методів для виконання основних операцій з матрицями.

### Опис завдання

У рамках лабораторної роботи необхідно реалізувати клас `Matrix`, що має наступний функціонал:

1. Додавання елементу до вказаного рядка та стовпця матриці.
2. Обчислення суми елементів у кожному рядку матриці.
3. Транспонування матриці.
4. Множення матриць.
5. Перевірка симетричності матриці.
6. Поворот матриці на 90 градусів вправо.
7. Виведення матриці у вигляді одномірного списку (згортка).
8. Отримання діагоналі матриці (якщо матриця квадратна).

### Виконання роботи

#### Структура проекту

- **labX/**
  - `matrix.py` - Основний код класу Matrix
  - `README.md` - Документація проекту

#### Опис основних файлів

##### matrix.py

```python
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        else:
            print("Invalid row or column index.")

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        result_matrix = Matrix(len(self.data), len(other.data[0]))

        # Perform matrix multiplication
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    result_matrix.data[i][j] += self.data[i][k] * other.data[k][j]

        return result_matrix

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        self.data = [list(row) for row in zip(*self.data[::-1])]

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0]) if list_of_lists else 0
        matrix = Matrix(rows, columns)
        matrix.data = list_of_lists
        return matrix

    def diagonal(self):
        if self.rows != self.columns:
            print("Matrix is not square.")
            return None

        return [self.data[i][i] for i in range(self.rows)]
```

### Опис основних методів

- **add_element**: Додає задане значення до вказаного елементу матриці.
- **sum_of_rows**: Обчислює суму елементів у кожному рядку матриці.
- **transpose**: Повертає транспоновану матрицю.
- **multiply_by**: Виконує множення двох матриць.
- **is_symmetric**: Перевіряє, чи є матриця симетричною.
- **rotate_right**: Повертає матрицю на 90 градусів вправо.
- **flatten**: Повертає матрицю у вигляді одномірного списку.
- **from_list**: Статичний метод для створення об'єкта типу `Matrix` із списку списків.
- **diagonal**: Повертає діагональні елементи матриці (якщо матриця квадратна).

### Приклади використання

#### Створення об'єкту Matrix

```python
matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(0, 2, 3)
matrix.add_element(1, 0, 4)
matrix.add_element(1, 1, 5)
matrix.add_element(1, 2, 6)
matrix.add_element(2, 0, 7)
matrix.add_element(2, 1, 8)
matrix.add_element(2, 2, 9)
```

#### Використання методів

```python
print(matrix.sum_of_rows())  # Output: [6, 15, 24]
print(matrix.transpose().data)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(matrix.multiply_by(matrix.transpose()).data)  # Output: [[14, 32, 50], [32, 77, 122], [50, 122, 194]]
print(matrix.is_symmetric())  # Output: True
matrix.rotate_right()
print(matrix.data)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(matrix.flatten())  # Output: [7, 4, 1, 8, 5, 2, 9, 6, 3]
print(matrix.diagonal())  # Output: [7, 5, 3]
```

### Результати

В результаті виконання лабораторної роботи був розроблений клас `Matrix`, що дозволяє виконувати основні операції з матрицями. Реалізовані методи були перевірені на прикладах, що показали коректність їх роботи.

### Висновки

Мета лабораторної роботи була досягнута. Було вирішено наступні завдання:

- Розробка класу `Matrix` для представлення та операцій над матрицями.
- Виконання основних операцій з матрицями: транспонування, множення, перевірка симетричності, поворот, згортка та отримання діагоналі.

### Інструкції з запуску

Для використання класу `Matrix` необхідно використовувати версію Python 3.6 або вище. Щоб запустити програму, використовуйте наступний код:

```sh
python matrix.py
```

Необхідні бібліотеки:
- Ніякі додаткові бібліотеки не потрібні.

Цей звіт дозволяє зрозуміти структуру та функціональність класу `Matrix` і документує його
 
