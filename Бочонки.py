import random
import logging
from datetime import datetime

logging.basicConfig(filename='Бочонки.log', level=logging.DEBUG)

def create_barrel_bag(N):
    return list(range(1, N+1))

def pull_barrel(barrel_bag):
    if len(barrel_bag)>0:
        pulled_barrel = random.choice(barrel_bag)
        barrel_bag.remove(pulled_barrel)
        logging.info(f'Вытянут бочонок: {pulled_barrel}')
        return pulled_barrel
    else:
        logging.info('Бочонков в мешке больше нет.')
        return None

def s_polsovatel():
    while True:
        try:
            N = int(input("Введите количество бочонков в мешке: "))
            if N<1:
                print("Количество бочонков должно быть больше 0")
                logging.error("Бочонков должно быть больше 0:")
            else:
                return N
        except ValueError:
            print("Пожалуйста, введите натуральное число.")
            logging.error(f"Введите натуральное число: {N}")

def main():
    N = s_polsovatel()
    logging.info(f'Запуск программы для N = {N},in {datetime.now()}')
    barrel_bag = create_barrel_bag(N)
    random.shuffle(barrel_bag)
    print("Вытаскиваем бочонки из мешка!")
    while barrel_bag:
        input("Нажмите Enter, чтобы вытянуть бочонок:")
        pulled_barrel = pull_barrel(barrel_bag)
        if pulled_barrel:
            print(f"Вы вытянули бочонок с номером: {pulled_barrel}")
            logging.info(f"Вы вытянули бочонок с номером: {pulled_barrel} in {datetime.now()}")


if __name__ == "__main__":
    main()
