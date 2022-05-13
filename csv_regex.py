import re


def csv_regex(csv):
    x = re.search("\.csv", csv)

    if x != None:
        return 1
    if x == None:
        return 0


if __name__ == '__main__':
    csv_regex("https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03")