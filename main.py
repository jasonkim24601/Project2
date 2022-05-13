# Original idea: https://www.youtube.com/watch?v=RvCBzhhydNk (Webscraping)
# Additional features: GUI, pandas library usage, regex, OS library


from controller import *


# Links to process:
# https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-preliminary-2022-05-03
# https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-challenge-2022-05-09?xd12
# https://magic.wizards.com/en/articles/archive/mtgo-standings/modern-showcase-challenge-2022-05-08?xd28



def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
