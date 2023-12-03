import re

"""завдання 17.14"""
def remove_duplicates_and_sort(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        unique_words = list(set(result))
        return sorted(unique_words)

    return wrapper

@remove_duplicates_and_sort
def get_words_from_file(file_path):
    words = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(re.findall(r'\b\w+\b', line.lower()))
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")

    return words

file_path = 'file.txt'
result = get_words_from_file(file_path)
print("Список слів без повторів, відсортований за алфавітом:", result)
