def eqv(a, b, c):
    eps = max(a, b) * 0.0001  # 0.01%
    return abs(a + b - c) < eps


def main():
    a = 0  #
    b = 0  # менять числа здесь
    c = 0  #
    print(eqv(a, b, c))


if __name__ == '__main__':
    main()