
Трубочки = {'Яйцо': 0.2, 'Сахар': 10.0, 'Мука': 10.0, 'Масло П.': 2.0}

def main():
    while True:
        look_for_rec()

def look_for_rec():
    look = input('Введите название рецепта: ')
    if look == 'Трубочки':
        ask = int(input('Введите количество: '))
        for key in Трубочки:
            value = Трубочки[key]
            print(key, value * ask)
    else:
        print('Простите, такого рецепта нет. Введите название рецепта с большой буквы')


if __name__ == "__main__":
    main()