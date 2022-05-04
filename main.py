import requests
from bs4 import BeautifulSoup
import CSV_To_txt


def main():
    URL = "https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # raw dump with no formatting
    with open("rawdump.txt", "w", encoding="utf-8") as file:
        file.write(str(page.text))
    # raw dump but with soup
    with open("soupdump.txt", "w", encoding="utf-8") as file:
        file.write(str(soup))
    # raw text dump
    with open("souptextdump.txt", "w", encoding="utf-8") as file:
        for line in str(soup.get_text()):
            line.strip()
            file.write(line)

    file.close()



if __name__ == '__main__':
    main()


