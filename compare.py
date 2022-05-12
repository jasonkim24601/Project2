import csv


def compare():
    card_filename = 'cardnames.csv'
    scraped_filename = 'souptextdump.csv'

    with open(card_filename, 'r') as f:
        hosts = f.readlines()

    with open(scraped_filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()


    for line in lines:
        for host in hosts:
            if host == line:

                print(line)






    # csvfile = open('cards.csv', 'r')
    #
    # csvreader = csv.reader(csvfile, delimiter=',')
    # for line in csvreader:
    #     print(line)
    #
    # csvfile.close()


if __name__ == '__main__':
    compare()
