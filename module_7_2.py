def custom_write(file_name, strings):
    # Словарь для хранения начала байтов и строк
    strings_positions = {}

    # Открываем файл для записи в кодировке UTF-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings):
            # Запоминаем текущую позицию в байтах
            byte_position = file.tell()
            # Записываем строку в файл с новой строки
            file.write(string + '\n')
            # Сохраняем номер строки (индекс + 1) и позицию байта в словаре
            strings_positions[(index + 1, byte_position)] = string

    return strings_positions


# Пример использования программы
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Выводим результат на консоль
for elem in result.items():
    print(elem)