import random


class Main:
    def game(self):
        count = 0
        print("Сейчас будет сгенерированно число от 1 до n. Попробуйте угадать")
        print('Введите n')
        n = int(input())
        number = random.randint(1, n)
        print('Введите ваше предполагаемое чиcло')
        maybeNumber = input()
        while True:
            if self.is_valid(maybeNumber, n):
                maybeNumber = int(maybeNumber)
                break
            else:
                print('А может быть все-таки введем целое число от 1 до ' + str(n) + '?')
                maybeNumber = input()

        while True:

            if maybeNumber < number:
                print("Слишком мало, попробуйте еще раз")
                maybeNumber = int(input())
                count += 1
            elif maybeNumber > number:
                print('Слишком много, попробуйте еще раз')
                maybeNumber = int(input())
                count += 1
            elif maybeNumber == number:
                print('Вы угадали, поздравляем!')
                print("Количество попыток =", count)
                print("Хотите ещё сыграть? (Да - y, Нет - любой символ ) ")
                var = input()
                if var == 'y':
                    self.game()
                    break
                else:
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    break

    def magic(self):
        answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
                  "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
                  "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
                  "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
                  "Перспективы не очень хорошие", "Весьма сомнительно"]
        print("Магический шар предсказаний")
        while True:
            print("Задай свой вопрос, так чтобы ответ был 'Да' или 'Нет'")
            input()
            print(random.choice(answer))
            print("Ещё вопрос? (Да - y, Нет - любой символ )")
            var = input()
            if var == 'y':
                self.magic()
                break
            else:
                print('Возвращайся если возникнут вопросы!')
                break

    def is_valid(self, string, integer):
        if string.isdigit() and 0 <= int(string) <= integer:
            return True
        else:
            return False

    def generate_password(self):
        DIGITS = '0123456789'
        ALPHA_LOWER = 'abcdefghijklmnopqrstuvwxyz'
        ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        SYMBOLS = "!#$%&*+-=?@^_"
        chars = ''
        passwords = []
        print("Введите количество паролей для генерации")
        count = int(input())
        print("Введите длину паролей для генерации")
        length = int(input())
        print("Включать ли цифры 0123456789? (Да - y, Нет - любой символ )")
        if input() == "y":
            chars += DIGITS
        print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (Да - y, Нет - любой символ )")
        if input() == "y":
            chars += ALPHA_UPPER
        print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (Да - y, Нет - любой символ )")
        if input() == "y":
            chars += ALPHA_LOWER
        print("Включать ли символы !#$%&*+-=?@^_? (Да - y, Нет - любой символ )")
        if input() == "y":
            chars += SYMBOLS
        print("Исключать ли неоднозначные символы il1Lo0O? (Да - y, Нет - любой символ)")
        if input() == "y":
            for c in 'il1Lo0O':
                if c in chars:
                    chars.replace(c, '')
        for _ in range(count):
            passwords.append(''.join(random.sample(chars, length)))
        print("Cгенерированные пароли:")
        print(passwords)

    def cesar(self):
        print("Шифр Цезаря")
        text = list()
        alphabetL, alphabetU = [], []
        print("Русский алфавит или английский? (Русский (без ё)  - r, Английский - любой символ)")
        if input() == 'r':
            alphabetL.extend('абвгдежзийклмнопрстуфхцчшщъыьэюя')
            alphabetU.extend("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
        else:
            alphabetL.extend('abcdefghijklmnopqrstuvwxyz')
            alphabetU.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        print("Зашифровать или расшифровать? (Зашифровать - z, Расшифровать - любой символ)")
        if input() == 'z':
            flag = True
        else:
            flag = False
        print('Знаете сдвиг?(Да - y, Нет - любой символ)')
        if input() == 'y':
            print("Введите сдвиг (число)")
            shift = int(input())
            flagS = True
        else:
            flagS = False
        print("Введите текст")
        text.extend(input())
        if not flagS:
            for shift in range(26):
                self.cesar_mini(shift, flag, alphabetU, alphabetL, text)
        else:
            self.cesar_mini(shift, flag, alphabetU, alphabetL, text)

    def cesar_mini(self, shift, flag, alphabetU, alphabetL, text):
        s = ''
        if flag:
            for c in text:
                if c in alphabetU:
                    s += alphabetU[(alphabetU.index(c) + shift) % len(alphabetU)]
                elif c in alphabetL:
                    s += alphabetL[(alphabetL.index(c) + shift) % len(alphabetL)]
                else:
                    s += c
        else:
            for c in text:
                if c in alphabetU:
                    s += alphabetU[(alphabetU.index(c) - shift) % len(alphabetU)]
                elif c in alphabetL:
                    s += alphabetL[(alphabetL.index(c) - shift) % len(alphabetL)]
                else:
                    s += c
        print(s)

    def display_hangman(self, tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''',
            # голова, торс, обе руки, одна нога
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            ''',
            # голова, торс, обе руки
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            ''',
            # голова, торс и одна рука
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            ''',
            # голова и торс
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            ''',
            # голова
            '''
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            ''',
            # начальное состояние
            '''
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            '''
        ]
        return stages[tries]
    def game_words(self):
        count = 0
        counter = 0
        words = ['собака', 'санитар', 'больница', 'программа']
        print("Угадайте слово")
        word = random.choice(words)
        word_a = ["." for _ in range(len(word))]
        print(word_a)
        flag = True
        while flag:
            if not '.' in word_a:
                print()
                print('Поздравляем вы угадали слово:')
                print(word)
                break
            print('Введите букву')
            alpha = input()
            if alpha in word:
                print('Есть такая буква')
                counter += 1
                for i in range(len(word)):
                    if alpha == word[i]:
                        word_a[i] = alpha
                print(word_a)
            else:
                print('Нет такой буквы')
                count -= 1
                print(self.display_hangman(count))
                print(word_a)
                if count == -7:
                    print("Игра закончилась. Вы мертвы")
                    break







while True:
    print()
    print('Меню')
    print('0 - Выход')
    print('1 - Угадайка чисел')
    print('2 - Магический шар')
    print('3 - Генератор паролей')
    print('4 - Шифр Цезаря')
    print('5 - Угадайка слова')
    a = int(input())
    obj = Main()
    if a == 0:
        exit()
    elif a == 1:
        obj.game()
    elif a == 2:
        obj.magic()
    elif a == 3:
        obj.generate_password()
    elif a == 4:
        obj.cesar()
    elif a == 5:
        obj.game_words()
