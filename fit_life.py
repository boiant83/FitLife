"""Проект FitLife - MVP версия 1.0."""

# 1. Знакомство с пользователем

# Имя пользователя
user_name = input('Ваше имя: ')
# Возраст пользователя
while True:
    user_age_int = input('Сколько вам лет: ')
    try:
        user_age = int(user_age_int)
        break
    except ValueError:
        print('\nЭто не число. Попробуйте снова - пример: 43')
        print("-" * 45)

# 2. Сбор данных для расчетов

# Вес пользователя
while True:
    user_weight_str = input('Ваш вес в кг: ')
    user_weight_str = user_weight_str.replace(',', '.')
    try:
        user_weight = float(user_weight_str)
        break
    except ValueError:
        print('\nЭто не число. Попробуйте снова - пример: 72.5')
        print("-" * 45)
# Рост пользователя
while True:
    user_height_str = input('Ваш рост в метрах: ')
    user_height_str = user_height_str.replace(',', '.')
    try:
        user_height = float(user_height_str)
        break
    except ValueError:
        print('\nЭто не число. Попробуйте снова - пример: 1.72')
        print("-" * 45)

# 3. Рассчеты для вывода

# Рассчет ИМТ (Индекс массы тела)
user_bmi = user_weight / user_height ** 2
user_bmi = round(user_bmi, 1)

# Рассчет кол-ва воды на массу тела
WATER_PER_KG = 30
ML_PER_LITER = 1000
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER
water_l = round(water_l, 2)

# Вывод результата расчетов
print('=' * 45)
print(f'\nОтчет для пользователя: {user_name} ({user_age} лет)')
print('Твой Индекс Массы Тела: ', user_bmi)
print(f'Норма воды: {water_l} л. воды в день\n')
print('Расчет закончен. Будь здоровым, и красивым!\n')
print('=' * 45)
