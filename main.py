import requests
from bs4 import BeautifulSoup


def main():
    URL = "https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # output_file = open("output.txt", "w")
    # # soup_string = str(soup)
    # # output_file.write(soup_string)
    # # output_file.close()
    #
    # # for link in soup.get_text():
    # #     soup_link = str(link)
    # #     print(soup_link)
    # #     output_file.write(soup_link)
    #
    # with open(output_file, "output.txt", encoding="utf-8") as f:
    #     f.write(soup)

    with open("rawdump.txt", "w", encoding="utf-8") as file:
        file.write(str(page.text))

    with open("soupdump.txt", "w", encoding="utf-8") as file:
        file.write(str(soup))

    with open("souptextdump.txt", "w", encoding="utf-8") as file:
        file.write(str(soup.get_text()))


    print(soup.get_text())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
