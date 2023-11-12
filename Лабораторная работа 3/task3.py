# TODO  Напишите функцию count_letters
def count_letters(text):
    dict_of_letters = {}
    text_low = text.lower()
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in text_low:
        if i in alphabet:
            if i not in dict_of_letters:
               dict_of_letters[i] = 1
            else:
                dict_of_letters[i] += 1
    return dict_of_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(text, dict_of_letters):
    number = len(text.replace(' ', ''))
    dict_of_frequency = {}
    for i in dict_of_letters:
        dict_of_frequency[i] = round(dict_of_letters[i] / number, 2)
    return dict_of_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_letters = count_letters(main_str)
dict_frequency = calculate_frequency(main_str, dict_letters)
for letter, frequency in dict_frequency.items():
    print(f'{letter}: {frequency:.2f}')