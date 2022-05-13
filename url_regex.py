import re


def url_regex(url):
    x = re.search("(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", url)

    if x != None:
        return True
    if x == None:
        return False


if __name__ == '__main__':
    url_regex("https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03")
