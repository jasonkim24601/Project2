import re


def csv_regex(csv):
    x = re.search("\.csv$", csv)

    if x != None:
        return 1
    else:
        return 0



if __name__ == '__main__':
    csv_regex("sneed.csv")
