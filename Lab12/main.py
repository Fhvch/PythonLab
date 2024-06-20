class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

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
