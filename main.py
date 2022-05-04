import requests
from bs4 import BeautifulSoup


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



        # file.write(str(soup.get_text()))
    # cleaning up

    file = open("souptextdump.txt", 'r', encoding="utf-8")
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == '' or line == "/n":
            pass
        else:
            print(line)
    file.close()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
