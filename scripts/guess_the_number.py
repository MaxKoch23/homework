
import random

number_to_guess = random.randint(1, 100)
print('Я загадал число от 1 до 100. Попробуй угадать!')

while True:
    guess = int(input('Введите ваше предположение:'))
    if guess < number_to_guess:
        print('Больше!')
    elif guess > number_to_guess:
        print('Меньше!')
    else:
        print('Поздравляю, вы угадали!')
        break