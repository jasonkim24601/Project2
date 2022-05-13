import pandas as pd


def CSV_to_txt() -> None:
    """
    Converts the cardnames.csv file to a csv file just containing the column containing card names.
    """
    csvfile = pd.read_csv('cards.csv')
    nameColumn = list(csvfile['name'])
    e = '\n'.join(map(str, nameColumn))
    print(e)
    with open("cardnames.csv", "w", encoding="utf-8") as file:
        file.write(e)


if __name__ == '__main__':
    CSV_to_txt()
