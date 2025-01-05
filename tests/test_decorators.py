from src.decorators import log


def test_log():
    """ тест на проверку правильности работы декоратора без добавления в модуль для логов """
    @log()
    def add(x, y):
        return x + y

    assert add(4, 5) == 9


def test_log_filename():
    """ тест на проверку правильности работы декоратора добавлением в определенный модуль для логов """
    @log("log_file")
    def add(x, y):
        return x + y

    assert add(4, 5) == 9
