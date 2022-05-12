import csv


def compare():
    card_filename = 'cardnames.csv'
    scraped_filename = 'souptextdump.csv'

    with open(card_filename, 'r') as f:
        cardlist_cards = f.readlines()

    with open(scraped_filename, 'r', encoding="utf-8") as f:
        scraped_cards = f.readlines()

    # list to store matches and to be used for writing
    write_list = []

    # open output file here
    with open("tournament_cards.csv", 'w', newline='\n') as f:

        # open raw scrape data
        for scrape_line in scraped_cards:
            # open processed card list data
            for card_line in cardlist_cards:
                # If an actual card is found on the scraped csv:
                if card_line == scrape_line:
                    print(scrape_line)

                    csvwriter = csv.writer(f)
                    csvwriter.writerow([scrape_line])



                    # This works but isn't escaping commas
                    # f.write(scrape_line)





if __name__ == '__main__':
    compare()
