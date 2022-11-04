from Iterator import iterator


def main():
    print('Начало. Введите метку (cat/dog)')
<<<<<<< HEAD
    mark = input()
=======
    mark=input()
>>>>>>> 9d865f6748297b743a2f4bdb78f255f70a0caac8
    val = iterator('annotation.csv', mark)
    for way in val:
        print(way)
    print('Конец')


if __name__ == "__main__":
    main()
