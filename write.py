import csv


def write(outputFile) -> None:
    """
    Method to see what parts of the scraped data are actually cards.
    Once the cards are pulled, append them to tournament_cards.csv
    :param outputFile: .csv file to write to
    """
    card_filename = 'cardnames.csv'
    scraped_filename = 'souptextdump.csv'


    with open('cardnames.csv', 'r') as f:
        cardlist_cards = f.readlines()

    with open('souptextdump.csv', 'r', encoding="utf-8") as f:
        scraped_cards = f.readlines()

    # open output file here
    with open(outputFile, 'a') as f:
        csvwriter = csv.writer(f)

        # open raw scrape data
        for scrape_line in scraped_cards:
            # open processed card list data
            for card_line in cardlist_cards:
                # If an actual card is found on the scraped csv:
                if card_line == scrape_line:
                    print(scrape_line)
                    csvwriter.writerow([scrape_line])

    with open(outputFile, 'r') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        return [[x.strip() for x in row] for row in reader]



if __name__ == '__main__':
    write("default.csv")
