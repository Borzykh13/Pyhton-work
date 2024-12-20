import matplotlib.pyplot as plt
import pandas as pd
import requests
import numpy as np

# Matplotlib — это библиотека для визуализации данных в Python. Она используется для создания любых видов графиков:
# линейных, круговых диаграмм, построчных гистограмм и других — в зависимости от задач

x = [1, 2, 3, 4, 5]
y = [2, 10, 5, 10, 2]

plt.plot(x, y, marker='1')

plt.title('график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
print("\n код matplotlib  \n")

# Pandas — это библиотека в Python, которая предназначена для анализа уже структурированных данных. Функциональность
# pandas включает в себя преобразование данных. Например, при помощи pandas можно сортировать строки и выделять
# подмножества, вычислять сводную статистику, например, среднее значение, изменять формы фреймов и объединять их.

Data = [1, 3, 4, 5, 6, 2, 9]
s = pd.Series(Data)
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas  \n")

# Requests — это библиотека в Python, которая позволяет взаимодействовать с веб-ресурсами и глобальной сетью.
# Она предоставляет разработчику обширный пул функций для работы со всеми видами HTTP-запросов.

import requests

# URL для запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Отправка GET-запроса
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Вывод данных в консоль
    data = response.json()  # Преобразование ответа в JSON
    for post in data:
        print(f"Title: {post['title']}\nBody: {post['body']}\n")
else:
    print(f"Ошибка при запросе данных: {response.status_code}")

# NumPy — это библиотека Python с открытым исходным кодом, которая широко используется в науке и инженерии.
# Библиотека NumPy содержит многомерные структуры данных, такие как однородные N-мерные ndarray, и большую библиотеку
# функций, которые эффективно работают с этими структурами данных.

import numpy

a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape)  # вывод колличества строк и столбцов

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)  # вывод таблицы из списков
print(a.shape)  # вывод колличества строк и столбцов

print(np.linspace(0, 10, num=10))  # вывод линейного массива через указанный интервал
