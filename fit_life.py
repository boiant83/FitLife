"""Проект FitLife - MVP версия 1.0."""

# 1. Знакомство с пользователем

# Имя пользователя
while True:
    user_name = input('Ваше имя: ').strip()
    if user_name == '':
        print('\nИмя не может быть пустым. Попробуйте снова.')
        print('-' * 45)
        continue
    break

# Возраст пользователя
while True:
    user_age_int = input('Сколько вам лет: ')
    try:
        user_age = int(user_age_int)
    except ValueError:
        print('\nЭто не число. Попробуйте снова (пример: 43)')
        print('-' * 45)
        continue
    if user_age < 1 or user_age > 120:
        print('\nВозраст должен быть от 1 до 120 лет. Попробуйте снова.')
        print('-' * 45)
        continue
    break

# 2. Сбор данных для расчётов

# Вес пользователя
while True:
    user_weight_str = input('Ваш вес в кг: ').replace(',', '.')
    try:
        user_weight = float(user_weight_str)
    except ValueError:
        print('\nЭто не число. Попробуйте снова (пример: 72.5)')
        print('-' * 45)
        continue
    if user_weight < 1 or user_weight > 500:
        print('\nВес должен быть от 1 до 500 кг. Попробуйте снова.')
        print('-' * 45)
        continue
    break

# Рост пользователя
while True:
    user_height_str = input('Ваш рост в метрах: ').replace(',', '.')
    try:
        user_height = float(user_height_str)
    except ValueError:
        print('\nЭто не число. Попробуйте снова (пример: 1.72)')
        print('-' * 45)
        continue
    if user_height < 0.5 or user_height > 2.5:
        print('\nРост должен быть от 0.5 до 2.5 м. Попробуйте снова.')
        print('-' * 45)
        continue
    break

# 3. Расчёты для вывода

# Расчёт воды
WATER_PER_KG = 30
ML_PER_LITER = 1000
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER
water_l = round(water_l, 2)

# Расчёт ИМТ
user_bmi = user_weight / user_height ** 2
user_bmi = round(user_bmi, 1)

# Оценка ИМТ по шкале ВОЗ
if user_bmi < 16:
    bmi_category = 'выраженный дефицит массы тела'
elif user_bmi < 18.5:
    bmi_category = 'недостаточная масса тела'
elif user_bmi < 25:
    bmi_category = 'норма'
elif user_bmi < 30:
    bmi_category = 'избыточная масса тела'
elif user_bmi < 35:
    bmi_category = 'ожирение 1 степени'
elif user_bmi < 40:
    bmi_category = 'ожирение 2 степени'
else:
    bmi_category = 'ожирение 3 степени'

# Подбор слова по возрасту
last_two = user_age % 100
last_one = user_age % 10

if 11 <= last_two <= 14:
    age_word = 'лет'
elif last_one == 1:
    age_word = 'год'
elif last_one in (2, 3, 4):
    age_word = 'года'
else:
    age_word = 'лет'

# Вывод
print('=' * 45)
print(f'Отчет для пользователя: {user_name} ({user_age} {age_word})')
print(f'Индекс массы тела: {user_bmi} — {bmi_category}.')
print(f'Суточная норма воды: {water_l} л.')
print()
print('Расчёт закончен. Здоровья вам!')
print('=' * 45)
