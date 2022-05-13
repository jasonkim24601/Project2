import re


def url_regex(url):
    """
    Method to check if input parameter is a URL.
    :param url: URL to run regex against
    :return: 1 if it is a URL, 0 otherwise
    """
    x = re.search("(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", url)

    if x != None:
        return 1
    if x == None:
        return 0


if __name__ == '__main__':
    url_regex("https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03")
