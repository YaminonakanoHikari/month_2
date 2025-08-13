from datetime import datetime as dt
from time import sleep
def checktime_befor_after(func):
    def wrapper(*args, **kwargs):
        # время до вызова
        start_time = dt.now()
        print(f"Функция была вызвана в {start_time.hour:02}:{start_time.minute:02}:{start_time.second:02} "
              f"{start_time.day:02}/{start_time.month:02}/{start_time.year}")
        #выполняем саму функцию
        result = func(*args, **kwargs)

        #время после вызова
        end_time = dt.now()
        print(f"Функция была закончены в {end_time.hour:02}:{end_time.minute:02}:{end_time.second}"
        f" {end_time.day:02}/{end_time.month:02}/{end_time.year}")

        return result #чтобы вернуть все, что вернула функция
    return wrapper

@checktime_befor_after
def hello_world():
    print("Hello World")
    sleep(1)

hello_world()