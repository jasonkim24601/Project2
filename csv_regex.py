import re


def csv_regex(csv):
    """
    Method to check if input parameter is in the filename.csv format
    :param csv: User input to run regex against
    :return: 1 if it is written in proper .csv format, 0 otherwise
    """
    x = re.search("\.csv$", csv)

    if x != None:
        return 1
    else:
        return 0


if __name__ == '__main__':
    csv_regex("sneed.csv")
