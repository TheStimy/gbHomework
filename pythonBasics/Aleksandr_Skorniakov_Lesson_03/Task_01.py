dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(word):
    if word.istitle():
        print(dictionary[word_lower].title())
    elif word.isupper():
        print(dictionary[word_lower].upper())
    else:
        print(dictionary[word_lower].lower())


input_word = input('Введите слово на английском: ')
word_lower = input_word.lower()

if word_lower in dictionary:
    num_translate(input_word)
else:
    print('Такого слова в словаре нет')
