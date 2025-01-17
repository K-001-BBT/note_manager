title = ['Основные темы', 'Персонажи', 'Рекомендации для чтения']
note = [
"Имя пользователя ",
"Содержание заметки",
'Описание заметки',
"Статус",
"Дата создания",
"Дата изменения",
]
username = input('Ведите имя: ')
title = input('Введите Заголовки заметки(одна из трех):\nОсновны темы\nПерсонажи\nРекомендации для чтения\n')
content = input('Введите задание: ')
status = input('Введите статус: ')
created_date = input('Введите дату начала в формате: день-месяц-год: ')
issue_date = input('Введите дату окончания в формате: день-месяц-год: ')
note1 = note.append(username)
note2 = note.append(title)
note3 = note.append(content)
note4 = note.append(status)
note5 = note.append(created_date)
note6 = note.append(issue_date)
print('\n'*3)
print(note[0], note[6])
print(note[1], note[7])
print(note[2], note[8])
print(note[3], note[9])
print(note[4], note[10])
print(note[5], note[11])

