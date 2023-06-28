class BasicWord:
    """Класс абстракция слов со списком подслов"""
    _src_word: str
    _subwords: list

    def __init__(self, src_word: str, subwords=[]):
        self._src_word = src_word
        self._subwords = [item.strip() for item in subwords if item.strip() != 'стоп']

    def __repr__(self):
        return f"Слово для проверки '{self.src_word}', количество подслов - {self.count_subwords}"

    def check_word(self, testword: str):
        """Возращает ИСТИНА если слово уже есть в списке подслов"""
        return testword in self._subwords

    def get_count_subwords(self):
        """Возвращает количесво элементов в списке подслов"""
        return len(self._subwords)

    def get_src_word(self):
        """Возвращает слово для тестирования"""
        return self._src_word

    # Свойства для доступа к полям класса
    count_subwords = property(get_count_subwords)
    src_word = property(get_src_word)
