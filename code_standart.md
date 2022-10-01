# Соблюдаемые правила оформления кода
---
## Отступы и переносы
---
- Используется 4 пробела (не табуляция) на каждый уровень отступа:
```python
if __name__ == '__main__':
    run()
```
- Используется отступ в 2 строки между верхнеуровневыми определениями функций или классами;
- 1 строка между определениями функций внутри класса;
- 1 строка для отделения логических фрагментов кода (субъективно на усмотрение):
```python
def get_a():
    letter_comparer = LetterComparer()
    print(str(letter_comparer))
class LetterComparer:
    def __init__(self):
        self.letter_a = "а"
        self.letter_b = "б"
        self.letter_c = "в"
        
        self.alphabet = "Кириллица"
   
    def __str__(self):
        return(f"{self.a} и {self.b}"P)
```
- Если строка слишком длинная (более 90 символов), то придерживаюсь следущего форматирование кода: 
- 1 отступ после переноса аргументов или выражения на следующей строке, если следующее выражение не переходит на новый уровень (перенос строки, аргументов, элементов списка и т.п.);
- в списках, словарях, аргументах функций, и т.п. каждый аргумент или элемент на отдельной строке; закрывающая скобка отдельно на новой строке;
```python
my_long_list = [
    "very_very_very_long_name_arg_1",
    "very_very_very_long_name_arg_2",
    "very_very_very_long_name_arg_3",
    "very_very_very_long_name_arg_4",
    "very_very_very_long_name_arg_5"
]
my_long_dictionary = {
    "very_very_very_long_key_1": "very_very_very_long_value_1",
    "very_very_very_long_key_2": "very_very_very_long_value_2",
    "very_very_very_long_key_3": "very_very_very_long_value_3",
    "very_very_very_long_key_4": "very_very_very_long_value_4",
    "very_very_very_long_key_5": "very_very_very_long_value_5"
}
function_with_large_list_of_args(
    very_very_very_long_name_arg_1,
    very_very_very_long_name_arg_2,
    very_very_very_long_name_arg_3,
    very_very_very_long_name_arg_4,
    very_very_very_long_name_arg_5
)
```
- 2 отступа после переноса аргументов или выражения на следующей строке, если следующее выражение переходит на новый уровень (при определении функции, блока if, т.е. там, где следом идет двоеточие);
```python
def function_with_large_list_of_args(
        very_very_very_long_name_arg_1,
        very_very_very_long_name_arg_2,
        very_very_very_long_name_arg_3,
        very_very_very_long_name_arg_4,
        very_very_very_long_name_arg_5):
    do_some_actions()
if some_very_very_long_statement or \
        one_more_very_very_long_statement or \
        last_very_very_very_long_statement:
    do_some_actions()
```
- Перенос строки осуществляется по логически законченной фразе, либо стараюсь максимально выровнять переносимые строки.
```python
my_long_string = "Very_very_very_long_sentence_1." \
    "One_more_very_very_very_long_sentence_2." \
    "Short_long_sentence_3." \
    "Unbelievable_very_very_very_very_very_very_long_sentence_4." \
    "Sentence_5."
    
my_second_long_string = "blablablablablablablablablablablablablabla" \
    "blablablablablablablablablablablablablablablablablablablablabla" \
    "blablablablablablablablablablablablablablablablablablablablabla" \
    "blablablablablablablablablablablablablablablablablablablablabla" \
    "blablablabla"
```
- Пустая новая строка в конце файла
---
## Нэйминг
---
- имя функций или переменных называю в нижнем регистре через нижнее подчеркивание:
```python
common_fields = "something"
def create_class_with_description(description):
    # ...
```
- имя констант называю в верхнем регистре через нижнее подчеркивание:
```python
ALLOWED_Ship_TYPES = ["liner", "tug", "tanker", "cruiser", "caravelle"]
```
- имя классов называю в 'CamelCase':
```python
class Plane(Transport):
    # ...
```
- в каждом имени стараюсь максимально передать суть:
- если это имя метода, то называю метод так, чтобы было понятно, что он делает:
```python
print_filtered_data(self):
    # ...
```
- если это имя переменной(или константы, или ключ словаря), то в названии обозначаю то, на что она ссылается
```python
common_fields = {value: line[index + 1] for index, value in enumerate(Transport.DEFAULT_FIELDS)}
description = {
    "class_name": line[0],
    "common_fields": common_fields,
    "unique_features": line[-1].lower()
}
transport_class = globals()[description["class_name"]]
    return transport_class.create_class_with_description(description)
```
- избегаю однобуквенных названий, непонятных сокращений и т.п.
---
## Пробелы
---
- при определении аргумента в определении функции '=' без пробелов:
```python
def function(min=0, max=1000):
# ...
```

- без пробелов перед и после скобок при вызове функции:
```python
function(min=100, max=200)
```
- без пробелов рядом со скобками внутри списка, словаря или кортежа:
```python
ALLOWED_Ship_TYPES = ["liner", "tug", "tanker", "cruiser", "caravelle"]
```
- пробел между операторами сложения, умножения и т.п., но без пробелов при логическом объединении каких-либо фрагментов выражения:
```python
summ = a + b
summ_and_mul = (a+b) * (c+d)
div_and_summ = a/b + c/d
```
