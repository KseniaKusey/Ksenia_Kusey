def buy_netflix(x, y, z, cost):
    # все возможные пары людей
    pairs = [(x, y), (x, z), (y, z)]
    # их суммы денег
    sums = [sum(pair) for pair in pairs]

    # ищем пару которая наиближе к значению подписки
    closest_diff = 9999999
    closest_pair = ()
    for i in range(len(pairs)):
        diff = abs(sums[i] - cost)
        if diff < closest_diff:
            closest_diff = diff
            closest_pair = pairs[i]

    # возвращаем имена тех, кто сможет купить подписку
    if closest_pair == (x, y):
        return "Алиса и Боб"
    elif closest_pair == (x, z):
        return "Алиса и Чарли"
    else:
        return "Боб и Чарли"


def main():
    x = 50  #
    y = 30  # менять числа здесь
    z = 20  #
    cost = 80  #
    print(buy_netflix(x, y, z, cost))


if __name__ == '__main__':
    main()
