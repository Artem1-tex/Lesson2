def first_word(text):
    """ Пошук першого слова
    Введіть слово або декілька
     """
    text = text.lstrip("., ")

    for s in [",", "."]:
        text = text.replace(s, " ")

    return text.split()[0]


assert first_word("Hello word") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word("..., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')

print(first_word("Hello word"))