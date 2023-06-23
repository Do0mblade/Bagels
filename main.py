
import random

NUM_DIGITS = 3 # размер секретного числа
MAX_GUESSES = 10 # количество попыток

def main():
    print(f"""
Bagels - дедуктивно-логическая игра.    
Ваш секретный код будет состоять из {NUM_DIGITS} символов.

В игре есть следующие подсказки:
    Pico    Одна цифра правильная, но в неправильном положении.
    Fermi   Одна цифра правильная и находится в правильном положении.
    Bagels  Ни одна цифра не является правильной.
    
Например, если секретное число было 248, а ваше предположение - 843, то ключом к разгадке будет Fermi Pico.
""")

    while True:
        # Переменная, в которой хранится секретное число, которое должен угадать игрок
        secretNum = getSecretNum()
        print('Число было загадано.')
        print('У тебя есть {} попыток, чтобы угадать число.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Попытка #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Правильно, выходим из цикла.
            if numGuesses > MAX_GUESSES:
                print('У тебя закончились попытки.')
                print('Числом было `{}`'.format(secretNum))

        # Спрашиваем игрока, хочет ли он сыграть еще раз.
        print('Хотите сыграть ещё раз? (да или нет)')
        if not input('> ').lower().startswith('д'):
            break
    print('Спасибо за игру!')

def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789') # Создает список цифр от 0 до 9.
    random.shuffle(numbers) # Перетасовываем их случайным образом.

    # Берем первые NUM_DIGITS цифр списка для нашего секретного числа:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа."""

    if guess == secretNum:
        return 'Ты выиграл!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # Правильных цифр нет вообще.
    else:
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный порядок ничего не выдавал.
        clues.sort()
        # Склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)




# Если программа не импортируется, а запускается, производим запуск:
if __name__ == '__main__':
    main()