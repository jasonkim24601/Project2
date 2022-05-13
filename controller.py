from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from url_regex import *
from csv_regex import *
from webscraper import *
from write import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.label_error.hide()
        self.label_done.hide()
        self.label_done2.hide()

        self.pButton_submit.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        # Hide everything again just in case user decides to run the program again without closing
        self.label_error.hide()
        self.label_done.hide()
        self.label_done2.hide()
        # Flag to end program as long as everything is okay.
        # If there's any number of error it will change to 0 and flag an error and prompt the user to fix errors.
        end_okay = 1
        # Variables to grab user input (if applicable)
        user_URL = None
        user_OUTPUT = None

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
        if end_okay == 1:
            try:
                f = open('cardnames.csv')
                f.close()
            except FileNotFoundError:
                end_okay = 0
                self.label_error.setText("cardnames.csv not found!")
                self.label_error.show()

        # If the user did put something in the output line, make sure they actually put a valid whatever.csv input.
        if end_okay == 1:
            if self.lineEdit_OUTPUT.text():
                csv = self.lineEdit_OUTPUT.text()
                if csv_regex(csv) == 0:
                    end_okay = 0
                    self.label_error.setText("Please enter your output as filename.csv or leave blank.")
                    self.label_error.show()
                if csv == "rawOutput.csv":
                    end_okay = 0
                    self.label_error.setText("Output .csv file cannot be named rawOutput.csv.")
                    self.label_error.show()

        # If everything goes through successfully...
        if end_okay == 1:
            # clear the error message popup
            self.label_error.hide()
            # Grab input from the URL line
            user_URL = self.lineEdit_URL.text()
            # Grab input from the output file line
            # If empty write to default.csv instead as stated on the GUI
            if self.lineEdit_OUTPUT.text():
                user_csv = self.lineEdit_OUTPUT.text()
            else:
                user_csv = "default.csv"
            # scrape website provided by user and save to souptextdump.csv
            webscaper(user_URL)
            # take that information and compare it to cardnames.txt and write to appropriate output .csv file.
            # this is done in write.py
            # if the output file is open it will throw a Permission Error, this catches it
            # OSError occurs when the provided filename.csv file has invalid characters
            # and the program can't save a file with that name (Think something like ???.csv)
            try:
                write(user_csv)
            except PermissionError:
                end_okay = 0
            except OSError:
                end_okay = 2

            if end_okay == 2:
                self.label_error.setText("Invalid output file name.")
                self.label_error.show()
            elif end_okay == 1:
                # Create done message with destination of output displayed
                doneText = "Done, results saved to "
                doneText += user_csv
                self.label_done.setText(doneText)

                self.label_done2.setText("Enter another website/output csv file or close.")

                self.label_done.show()
                self.label_done2.show()
            # If output file is open, do this
            else:
                self.label_error.setText("Output file is open, please close and try again.")
                self.label_error.show()

