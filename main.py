from webscraper import *
from CSV_To_txt import *
from compare import *


if __name__ == '__main__':
    webscaper("https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03")
    CSV_to_txt()
    compare()
