example_str = 'В строке, есть, ошибка, снова ошибка.'
result = example_str.replace(',', '.').replace('ошибка', 'исправление')
print(result)