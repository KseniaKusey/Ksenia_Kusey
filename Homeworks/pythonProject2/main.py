import random


def generate_list():
    new_list = []
    for i in range(random.randint(50, 100)):
        new_list.append(random.randint(0, 9999))
    return new_list


def main():
    list_1 = generate_list()
    list_2 = generate_list()
    main_list = list(set(list_1) - set(list_2))
    print(main_list)


def common_number(list_1, list_2):
    list_1_set = set(list_1)
    list_2_set = set(list_2)

    if (list_1_set & list_2_set):
        print(list_1_set & list_2_set)
    else:
        print("No common numbers")

