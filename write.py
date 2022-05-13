import csv
import os

def write(outputFile) -> None:
    """
    Method to see what parts of the scraped data are actually cards.
    Once the cards are pulled, append them to tournament_cards.csv
    It is tending to print to the .csv with an excessive amount of whitespace, so it first writes to rawOutput.csv
    And then it writes it again to the desired output file with the whitespace removed.
    :param outputFile: .csv file to write to
    """

    # import full list of card names
    with open('cardnames.csv', 'r') as f:
        cardlist_cards = f.readlines()
    # import full scraped dump
    with open('souptextdump.csv', 'r', encoding="utf-8") as f:
        scraped_cards = f.readlines()

    # It first will write to rawOutput.csv
    # It will then rewrite to the desired output file, with all the white space removed.
    with open("rawOutput.csv", 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["CARDS"])
        # open raw scraped data
        for scrape_line in scraped_cards:
            # open list of card names
            for card_line in cardlist_cards:
                # If an actual card is found on the scraped csv write it down
                if card_line == scrape_line:
                    scrape_line.strip()
                    print(scrape_line)
                    csvwriter.writerow([scrape_line])
    # Copying from rawOutput.csv to the desired final output destination
    with open("rawOutput.csv", newline='') as in_file:
        with open(outputFile, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)




if __name__ == '__main__':
    write("default.csv")
