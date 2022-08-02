
from datetime import timedelta,datetime
from datetime import date
from Person import Client
from Book import Book
import time
class Borrowing:

    def __init__(self, client, book):
        self._id = str(round(time.time()*1002))
        # math for get date
        self._date = datetime.now().date()
        seprateDate = datetime.strptime(str(self._date), "%Y-%m-%d")
        self._endDate = seprateDate + timedelta(days=10)
        self._idClient = client._id
        self._idBook = book._id
        self._status = "Active"
        print("An order with ID: %s has created" %self._id)

    def get_borrowed_book_id(self):
        return self._idBook

    def get_order_id(self):
        return self._id

    def get_client_id(self):
        return self._idClient

    def get_end_date(self):
        return self._endDate

    def get_init_date(self):
        return self._date

    def get_order_status(self):
        return self._status

    def set_status(self,status):
        self._status = status



    def get_order_details(self):
        return {
            "Order ID": self._id,
            "Start Date": self._date,
            "End Date": self._endDate,
            "Book ID": self._idBook,
            "Client ID": self._idClient,
            "Status": self._status
        }