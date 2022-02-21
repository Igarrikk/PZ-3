# Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(txt):
    word = txt[0].upper() + txt[1:]
    return word

string = input("Вводите слова, разделенные пробелом: ")
for word in string.split(' '):
    print(f'{int_func(word)} ', end='')
