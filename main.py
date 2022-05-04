import requests
from bs4 import BeautifulSoup



def main():


    URL = "https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03"
    page = requests.get(URL)

    # print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.get_text())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
