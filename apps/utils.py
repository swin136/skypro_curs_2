import requests
import inspect
import os
import random
from time import sleep
from apps import loger
from apps import basicword


# Каталог для хранения служебных файлов проекта
APPS_DIR = 'apps'
# Имя файла для хранения логов
LOG_FILE = 'data.log'

# Ссылка на JSON-ресурс
URL_SRC = 'https://jsonkeeper.com/b/CVW9'

# Заголовки для работы requests.get
HEADERS = {
    "Accept": "*/*",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}



def get_connection(url: str, site_headers: dict, attempts: int, is_log=True, verify=True):
    """
    Загружает данные с внешнего ресурса. При неудачной попытке загрузки осуществляется повтор.
    :param url: ссылка на ресурс с JSON-данными
    :param site_headers: заголовки из парсеров
    :param attempts: количество повторных попыток для доступа к ресурсу
    :param is_log: включение ведения логирования
    :param verify: включение проверки SSL-сертефиката
    :return: Response object (None в случае ошибок доступа)
    """
    try:
        response = requests.get(url=url, headers=site_headers, verify=verify)
        return response
    except Exception as e:
        if is_log:
            log = loger(os.path.join(APPS_DIR, LOG_FILE))
            log.write_log(f"При доступе к ресурсу {url} возникла ошибка: {type(e).__name__} >>> "
                          f"модуль {inspect.stack()[0][1]}: функция {inspect.stack()[0][3]}: "
                          f"строка {inspect.stack()[0][2]}")
        if attempts:
            sleep(3)
            get_connection(url=url, site_headers=site_headers, attempts=attempts - 1, is_log=is_log, verify=verify)
        else:
            return

def load_random_word():
    """
    Загружаем случайное слово с внешнего JSON-ресурса
    :return: экземпляр класса BasicWord (в слусе ошибки None)
    """
    # Получаем данные с внешнего ресурса
    response = get_connection(url=URL_SRC, site_headers=HEADERS, attempts=3, verify=False)
    if response is not None:
        try:
            # Считываем данные
            data = response.json()
            # Получаем случайное слово
            random_word = data[random.randint(0, len(data)-1)]
            return basicword(random_word['word'], random_word['subwords1'])
        # Обрабатываем исключения, записваем в логи, возвращаем None
        except requests.exceptions.JSONDecodeError as error:
            log = loger(os.path.join(APPS_DIR, LOG_FILE))
            log.write_log(f"При чтении данных JSON с ресурса {URL_SRC} возникла ошибка: "
                          f"{type(error).__name__} >>> модуль {inspect.stack()[0][1]}: "
                          f"функция {inspect.stack()[0][3]}: строка {inspect.stack()[0][2]}")
            return
        except TypeError as terror:
            log = loger(os.path.join(APPS_DIR, LOG_FILE))
            log.write_log(f"При преобразовании JSON-данных с ресурса {URL_SRC} возникла ошибка: "
                          f"{type(terror).__name__} >>> модуль {inspect.stack()[0][1]}: "
                          f"функция {inspect.stack()[0][3]}: строка {inspect.stack()[0][2]}")
            return

        except KeyError as keyerror:
            log = loger(os.path.join(APPS_DIR, LOG_FILE))
            log.write_log(f"Ошибка доступа к словарю с вопросами! "
                          f"{type(keyerror).__name__} >>> модуль {inspect.stack()[0][1]}: "
                          f"функция {inspect.stack()[0][3]}: строка {inspect.stack()[0][2]}")
            return

    print(f'Ошибка доступа к JSON-ресурсу {URL_SRC}')
    return


def hello_msg(username, testword, count_subwords):
    """
    Выводим привественное параметризированное сообщение пользователю.
    :param username: имя пользователя
    :param testword: слово для тестирования
    :param count_subwords: количество подслов, которое надо угадать пользователю
    :return: None
    """
    print(f"Привет, {username}!")
    print(f"Составьте {count_subwords} слов из слова {testword.upper()}")
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')
    print("Поехали, Ваше первое слово")