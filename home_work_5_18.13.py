
class SeqTxt:
    def __init__(self, data):
        self.data = data

    def seq_to_text(self):
        return ' '.join(map(str, self.data))

    def text_to_seq(self, text):
        return list(map(float, text.split()))


class TxtList(SeqTxt, list):
    def __init__(self, data):
        SeqTxt.__init__(self, data)
        list.__init__(self, data)


class TxtVector(TxtList):
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.seq_to_text())

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            text_data = file.read()
        self.data = self.text_to_seq(text_data)

    def scalar_product(self, other_vector):
        return sum(a * b for a, b in zip(self.data, other_vector.data))


class TxtMatrix(SeqTxt):
    def __init__(self, data):
        SeqTxt.__init__(self, data)
        self.vectors = [TxtVector(vector) for vector in data]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for vector in self.vectors:
                file.write(vector.seq_to_text() + '\n')

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        self.vectors = [TxtVector(SeqTxt(line.strip()).text_to_seq(line.strip())) for line in lines]

    def vector_matrix_product(self, vector):
        result_vector = TxtVector([sum(a * b for a, b in zip(row, vector.data)) for row in zip(*self.vectors)])
        return result_vector

    def matrix_vector_product(self, vector):
        result_vector = TxtVector([sum(a * b for a, b in zip(row, vector.data)) for row in self.vectors])
        return result_vector

    def matrix_matrix_product(self, other_matrix):
        result_matrix = TxtMatrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*other_matrix.vectors)] for row in self.vectors])
        return result_matrix


# Приклад використання класів
data_vector1 = [1.5, 2.3, 4.7]
data_vector2 = [0.5, 1.2, 3.4]
txt_vector1 = TxtVector(data_vector1)
txt_vector2 = TxtVector(data_vector2)

# a) Обчислити скалярний добуток
scalar_product_result = txt_vector1.scalar_product(txt_vector2)
print(f"Scalar Product Result: {scalar_product_result}")

data_matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
txt_matrix = TxtMatrix(data_matrix)

# Збереження матриці у файл
txt_matrix.save_to_file('matrix.txt')

# Створення та завантаження матриці з файлу
loaded_matrix = TxtMatrix([])
loaded_matrix.load_from_file('matrix.txt')

# Виведення зчитаної матриці
print(f"Loaded Matrix:")
for vector in loaded_matrix.vectors:
    print(vector)

# б) Обчислити добуток вектору на матрицю та зберегти у новому текстовому файлі
vector_matrix_product_result = loaded_matrix.vector_matrix_product(txt_vector1)
vector_matrix_product_result.save_to_file('vector_matrix_product.txt')

# в) Обчислити добуток матриці на вектор та зберегти у новому текстовому файлі
matrix_vector_product_result = loaded_matrix.matrix_vector_product(txt_vector1)
matrix_vector_product_result.save_to_file('matrix_vector_product.txt')

# г) Обчислити добуток матриць та зберегти у новому текстовому файлі
matrix_matrix_product_result = loaded_matrix.matrix_matrix_product(loaded_matrix)
matrix_matrix_product_result.save_to_file('matrix_matrix_product.txt')
