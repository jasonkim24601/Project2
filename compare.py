import csv


def compare(scrapetext) -> None:
    """
    Method to see what parts of the scraped data are actually cards.
    Once the cards are pulled, append them to tournament_cards.csv
    :param scrapetext: CSV file containing the names of the scraped data from the Wizard's Website.
    """
    card_filename = 'cardnames.csv'
    scraped_filename = 'souptextdump.csv'
    scraped_filename = scrapetext

    with open(card_filename, 'r') as f:
        cardlist_cards = f.readlines()

    with open(scraped_filename, 'r', encoding="utf-8") as f:
        scraped_cards = f.readlines()

    # open output file here
    with open("tournament_cards.csv", 'a', newline='\n') as f:
        csvwriter = csv.writer(f)

        # open raw scrape data
        for scrape_line in scraped_cards:
            # open processed card list data
            for card_line in cardlist_cards:
                # If an actual card is found on the scraped csv:
                if card_line == scrape_line:
                    print(scrape_line)

                    csvwriter.writerow([scrape_line])


if __name__ == '__main__':
    compare()
