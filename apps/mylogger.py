from datetime import datetime


class MyLoger:
    """
    Класс для сохранения логов работы программы. Лог сохранется в файл и также может выводиться на консоль.
    """
    _is_print: bool
    _file_log: str

    def __init__(self, file_log: str, is_print=True):
        """
        Конструктор экземпляра класса, передаем ему имя файла для записи логов, а также взводим (по умолчанию) флаг
        вывода текста лога на консоль.
        :param file_log:
        :param is_print:
        """
        self._is_print = is_print
        self._file_log = file_log
        self._type_msg = ("Error", "Info", "Debug")

    def get_filelog(self) -> str:
        """
        Возвращает имя файла для логировния
        :return:
        """
        return self._file_log

    def get_type_log(self, type_msg: int):
        """
        Возвращает тип лога по его индексу
        :param type_msg:
        :return:
        """
        try:
            return self._type_msg[type_msg]
        except IndexError:
            return self._type_msg[0]

    def is_print_console(self) -> bool:
        """
        Возвращает значение флага показа сообщений лога в консоли
        :return:
        """
        return self._is_print

    def write_log(self, log_msg: str, index_msg=0) -> None:
        """
        Пишет лог ошибки(сообщения в файл). Может также выводить текст на консоль.
        :param log_msg: сообщение лога
        :param index_msg: индекс для записи в лог его типа
        :return: None
        """
        # При необходимости вывожу сообщение на консоль
        if self.is_print_console():
            print(log_msg)
        try:
            with open(file=self.get_filelog(), mode="at", encoding="utf-8") as file:
                date = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
                file.write(f"{self.get_type_log(index_msg)}: {date} : {log_msg}\n")
        except IOError:
            print(f"Возникла ошибка ввода-вывода при попытке записи лога в файл {self.get_filelog()}")
