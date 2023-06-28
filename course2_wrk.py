from apps import player
from apps.utils import load_random_word
from apps.utils import hello_msg


def main():
    """Реализована бизнес-логика приложения"""
    # Загружаем слово для тестирования
    test_word = load_random_word()
    if test_word is None:
        print('Критическая ошибка! Работа программы будет завершена.')
        return

    # Получаем имя игрока
    username = ""
    while True:
        username = input('Ввведите имя игрока ').strip().capitalize()
        if username != '':
            break

    # Приветствуем пользователя
    hello_msg(username=username, testword=test_word.src_word, count_subwords=test_word.count_subwords)
    # Создаем класс для игрока
    session = player(username)

    # Начинаем цикл опроса пользователя
    while True:
        userword = input('Введите слово >>> ').strip().lower()
        # Пользователь ввел комбинация для выхода из цикла
        if userword == 'стоп' or userword == 'stop':
            break
        # Пользователь ввел слишко короткое слово
        if len(userword) < 3:
            print('Слишком короткое слово!')
            continue

        # Пользователь ввел слово повторно
        if session.check_word(userword):
            print(f"Слово {userword.upper()} уже использовано!")
            continue
        # Пользователь угадал слово
        if test_word.check_word(userword):
            print('Верно!')
            session.add_subword(userword)
            # Пользователь угадал все слова
            if session.use_words_count == test_word.count_subwords:
                # Идем на завершение цикла опроса
                break
            else:
                continue
        else:
            print('Неверно!')
            continue
    # Выводим статистику игры перед завершеним работы программы
    print(f'Игра завершена, Вы угадали {session.use_words_count} слов!')


if __name__ == "__main__":
    main()
