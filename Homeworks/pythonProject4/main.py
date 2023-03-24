import random


def magic(seq_len_min, seq_len_max, number_len_min, number_len_max, x):
    # число от 0 до 9999
    # длина последовательности - от 5 до 100
    sum = 0
    for i in range(random.randint(seq_len_min, seq_len_max)):
        sum += random.randint(number_len_min, number_len_max)
    return (sum % x == 0)


def main():
    x = int(input("Введите положительное число больше нуля"))

    if (x <= 0):
        return

    print("Ответ:", magic(5, 100, 0, 9999, x))


if __name__ == '__main__':
    main()