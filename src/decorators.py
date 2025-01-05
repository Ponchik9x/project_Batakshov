import os
from functools import wraps


def log(filename=None):
    """Декоратор-функция автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
            else:
                message = f"{func.__name__} ok"
            if filename:
                os.makedirs("logs", exist_ok=True)
                filepath = os.path.join("logs", f"{filename}.txt")
                with open(filepath, "a", encoding="utf-8") as file:
                    file.write(message + "\n")
            else:
                print(message)

            return result

        return inner

    return wrapper


@log("log_file")
def my_function(x, y):
    return x + y


print(my_function(4, 5))
