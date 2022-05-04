
import pandas as pd


def CSV_to_txt():

    csvfile = pd.read_csv('cards.csv')

    nameColumn = list(csvfile['name'])

    e = '\n'.join(map(str, nameColumn))

    print(a)
    print(e)


if __name__ == '__main__':
    CSV_to_txt()