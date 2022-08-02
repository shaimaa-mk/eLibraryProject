
import time
# declare a new class for book instance

class Book:

    def __init__(self, title, desc, author):
        self._id = str(round(time.time()*1011))
        self._title = title
        self._description = desc
        self._author = author
        self._status = "Active"
        print("An book with ID: %s has added" % self._id)

    # to query about book
    def get_bookid(self):
        return self._id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_author(self):
        return self._author

    def get_status(self):
        return self._status

    # to make change in book
    def set_title(self,title):
        self._title = title

    def set_description(self,desc):
        self._description

    def set_author(self,author):
        self._author = author

    def setstatus(self, status):
        self._status = status

    #To Display Book Details
    def get_book_detials(self):
        return {
            "id": self._id,
            "title": self._title,
            "description": self._description,
            "author": self._author,
            "status": self._status
        }







