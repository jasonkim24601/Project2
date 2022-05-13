from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from url_regex import *
from csv_regex.import *
from webscraper import *
from compare import *
import re


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_error.hide()
        self.label_done.hide()
        self.label_done2.hide()

        self.pButton_submit.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        # Flag to end program as long as everything is okay.
        end_okay = 1

        # Check to make sure URL is filled.
        if not self.lineEdit_URL.text():
            # If it isn't filled, show an error message.
            end_okay = 0
            self.label_error.setText("URL cannot be blank!")
            self.label_error.show()

        # Check to make sure URL provided is valid.
        if end_okay == 1:
            url = self.lineEdit_URL.text()
            if url_regex(url) == 0:
                end_okay = 0
                self.label_error.setText("Please enter a valid URL!")
                self.label_error.show()

        # Make sure cardnames.csv exists
        # This is the csv containing all the card names, no point scraping if
        # we have nothing to compare against to see if we scraped any cards.
        try:
            f = open('cardnames.csv')
            f.close()
        except FileNotFoundError:
            end_okay = 0
            self.label_error.setText("cardnames.csv not found!")
            self.label_error.show()

        # If the user did put something in the output line, make sure they actually put a valid whatever.csv input.
        if self.lineEdit_OUTPUT.text():



        # If everything goes through successfully...
        if end_okay == 1:
            # Grab input from the output file line
            # If empty write to output.csv instead.




            self.label_error.hide()
            self.label_done.show()
            self.label_done2.show()
