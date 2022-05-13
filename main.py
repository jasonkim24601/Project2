from webscraper import *
from CSV_To_txt import *
from compare import *

# Alternate URLs of different tournaments:
# https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-challenge-2022-05-09?xd12
# https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-showcase-challenge-2022-05-08?xd28


if __name__ == '__main__':
    webscaper("https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03")
    CSV_to_txt()
    compare("souptextdump.csv")
