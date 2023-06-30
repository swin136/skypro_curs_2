class Player:
    """Класс абстракции игрока"""
    _name: str
    _use_words: list

    def __init__(self, name: str):
        self._name = name.strip()
        self._use_words = []

    def __repr__(self):
        return f"Игрок {self.name}"

    def get_name(self) -> str:
        """Возращает имя игрока"""
        return self._name

    def get_use_words(self) -> list:
        """Возвращает список угаданных игроком слов"""
        return self._use_words

    def get_count_usewords(self) -> int:
        """Возвращает количесво угаданных игроком слов"""
        return len(self.use_words)

    def add_subword(self, word: str) -> None:
        """Добавляет слово в список угаданных игроком"""
        if not word.strip() in self.use_words:
            self.use_words.append(word.strip())

    def check_word(self, testword: str) -> bool:
        """Возращает ИСТИНА если слово уже есть в списке угаданных"""
        return testword in self.use_words

    # Свойства для доспупа к полям класса
    name = property(get_name)
    use_words = property(get_use_words)
    use_words_count = property(get_count_usewords)

