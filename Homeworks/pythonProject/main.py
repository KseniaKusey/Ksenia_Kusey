## +--------------------------------------------+
## |           |    V (м/с)    |    Sнач (м)    |
## +--------------------------------------------+
## |    Tom    |       y       |       0        |
## +--------------------------------------------+
## |   Jerry   |       x       |     0 + s      |
## +--------------------------------------------+
##
## Решение:
## 1) Определить V сближения двух объектолв (Тома и Джерри)
## 2) Поделить S начальное Джерри на полученное значение из пункта №1 (S / V = t)
##
## Возможные проблемы:
## 1) Если расстояние между объектами равно 0, то Том уже догнал Джерри
## 2) Если расстояние != 0, а скорость Джерри >= скорости Тома, то Том никогда не догонит Джерри
##

def main():
    Vx = int(input("Скорость Джерри: "))
    Vy = int(input("Скорость Тома: "))
    S = int(input("Расстояние между ними: "))

    # Возможно нам будет задано отрицательное значение S,
    # и это будет означать что том должен бежать в другую сторону
    # (По условию этого не сказано, но предусмотреть стоит)
    S = abs(S)

    if S == 0:
        print("Том догонит Джерри за 0 секунд")
    elif Vy <= Vx:
        print("Том никогда не догонит Джерри")
    else:
        Vc = Vy - Vx  # скорость сближение
        t = S / Vc  # время за которое Том догонит Джерри
        print(f"Том догонит Джерри за {t} секунд")


if __name__ == '__main__':
    main()