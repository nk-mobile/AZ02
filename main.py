# 1. Самостоятельно создайте DataFrame с данными
#
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
#
# 3. Вычислите среднюю оценку по каждому предмету
#
# 4. Вычислите медианную оценку по каждому предмету
#
# 5. Вычислите Q1 и Q3 для оценок по математике:
#
# Q1_math = df['Математика'].quantile(0.25)
#
# Q3_math = df['Математика'].quantile(0.75)
#
# - можно также попробовать рассчитать IQR
#
# 6. Вычислите стандартное отклонение


import pandas as pd
import numpy as np

# Загрузка данных из CSV-файла
df = pd.read_csv('таблица_оценок.csv', encoding='utf-8')
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
print(df.head())

# Переименование столбцов для удобства (если нужно)
df.columns = ['Студент', 'Предмет', 'Оценка']

# 3. Вычисление средней оценки по каждому предмету
average_by_subject = df.groupby('Предмет')['Оценка'].mean()
print("Средняя оценка по каждому предмету:")
print(average_by_subject.round(2))
print("\n" + "=" * 50 + "\n")

# 4. Вычисление медианной оценки по каждому предмету
median_by_subject = df.groupby('Предмет')['Оценка'].median()
print("Медианная оценка по каждому предмету:")
print(median_by_subject)
print("\n" + "=" * 50 + "\n")

# 5. Вычисление Q1, Q3 и IQR для оценок по математике (предполагая, что 'Математика' - это 'Математика' в данных)
# Найдем правильное название предмета
math_subject_name = None
for subject in df['Предмет'].unique():
    if 'Математика' in subject or 'мат' in subject.lower():
        math_subject_name = subject
        break

if math_subject_name:
    math_grades = df[df['Предмет'] == math_subject_name]['Оценка']

    Q1_math = math_grades.quantile(0.25)
    Q3_math = math_grades.quantile(0.75)
    IQR_math = Q3_math - Q1_math

    print(f"Статистика для предмета '{math_subject_name}':")
    print(f"Q1 (25-й перцентиль): {Q1_math}")
    print(f"Q3 (75-й перцентиль): {Q3_math}")
    print(f"IQR (интерквартильный размах): {IQR_math}")
else:
    print("Предмет 'Математика' не найден в данных. Доступные предметы:")
    print(df['Предмет'].unique())
print("\n" + "=" * 50 + "\n")

# 6. Вычисление стандартного отклонения по каждому предмету
std_by_subject = df.groupby('Предмет')['Оценка'].std()
print("Стандартное отклонение оценок по каждому предмету:")
print(std_by_subject.round(2))
