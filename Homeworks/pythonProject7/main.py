def search_substr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"


def main():
    subst = "apelsin"
    st = "yablokoapelsinmandarin"
    print(search_substr(subst, st))


if __name__ == '__main__':
    main()