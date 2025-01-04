from src.decorators import log


def test_log():
    @log()
    def add(x, y):
        return x + y

    assert add(4, 5) == 9


def test_log_filename():
    @log("log_file")
    def add(x, y):
        return x + y

    assert add(4, 5) == 9
