import requests
from bs4 import BeautifulSoup


def webscaper(URL) -> None:
    """
    Method to scrape URL passed to it as save it as a csv file.
    :param URL: URL to scrape
    """

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # # raw dump with no formatting
    # with open("rawdump.txt", "w", encoding="utf-8") as file:
    #     file.write(str(page.text))
    #
    # # raw dump but with soup
    # with open("soupdump.txt", "w", encoding="utf-8") as file:
    #     file.write(str(soup))

    # raw text dump done correctly
    with open("souptextdump.csv", "w", encoding="utf-8") as file:
        for line in str(soup.get_text()):
            line.strip()
            file.write(line)


if __name__ == '__main__':
    webscaper("https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03")
