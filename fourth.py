from Iterator import iterator


def main():
        print('Начало')
        val = iterator("annotation.csv", "cat")
        for way in val:
            print(way)
        print('Конец')


if __name__ == "__main__":
        main()