expenses = []

while True:
    print('\nМеню')
    print('1. Добавить расход')
    print('2. Показать все расходы')
    print('3. Показать общую сумму')
    print('4. Выйти')
    choice = input('Выберите действие 1-4')

    if choice == '1':
        category = input('Введите категорию расхода')
        amount = float(input('Введите сумму расхода'))
        expenses.append((category, amount))
        print(f'Добавлено: {category} - {amount}')
    elif  choice == '2':
        if not expenses:
            print('Нет записанных расходов')
        else:
            for i, (category, amount) in enumerate(expenses, start=1):
                print(f'{i}. {category} - {amount}')
    elif choice == '3':
        total = sum(amount for _, amount in expenses)
        print(f'Общая сумма расходов: {total}')
    elif choice == '4':
        print('Выход из программы.')
        break
    else:
        print('Неверный ввод. Попробуйте снова')

