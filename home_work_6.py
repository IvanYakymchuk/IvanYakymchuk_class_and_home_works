import re

"""завдання 21.10"""
def calculate_emotion_index(chat_text):
    words = []
    simple_emoticons = 0
    intense_emoticons = 0


    words = re.findall(r'\b\w+\b', chat_text.lower())


    simple_emoticons += len(re.findall(r'(\:\){1,2}\s|\:\({1,2}\s)', chat_text))
    print(re.findall(r'(\:\){1,2}\s|\:\({1,2}\s)', chat_text))
    intense_emoticons += len(re.findall(r'(\:\){3,}\s|\:\({3,}\s)', chat_text))
    print(re.findall(r'(\:\){3,}\s|\:\({3,}\s)', chat_text))
    total_words = len(words)
    total_emoticons = simple_emoticons + intense_emoticons
    emotion_index = total_emoticons / total_words if total_words != 0 else 0
    simple_emoticons_coeff = 1
    intense_emoticons_coeff = 2
    weighted_emotion_index = (simple_emoticons_coeff * simple_emoticons +
                              intense_emoticons_coeff * intense_emoticons) / total_words if total_words != 0 else 0
    return emotion_index, weighted_emotion_index, total_words, total_emoticons, simple_emoticons, intense_emoticons


file_path = 'text.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    chat_text = file.read()


index, weighted_index, total_words, total_emoticons, simple_emoticons, intense_emoticons = calculate_emotion_index(chat_text)
print("Індекс емоційності:", index)
print("Взважений індекс емоційності:", weighted_index)
print("Загальна кількість слів:", total_words)
print("Загальна кількість емоційних смайлів:", total_emoticons)
print("Кількість простих емоційних смайлів:", simple_emoticons)
print("Кількість винятково емоційних смайлів:", intense_emoticons)