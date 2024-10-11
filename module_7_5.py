import time
import os

for directory in os.walk('.'):
    for root, dirs, files in os.walk('.'):
        for file in files:
            filepath = os.path.join(str(directory))
            filetime = os.path.getmtime('.')
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize('.')
            parent_dir = os.path.dirname(r'C:\ДЗ\pythonProject1\module_7_5.py')
for dirpath, dirnames, filenames in os.walk('.'):
    for file in filenames:
        if file == 'workspace.xml':
            continue
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
            f' Родительская директория: {parent_dir}')
