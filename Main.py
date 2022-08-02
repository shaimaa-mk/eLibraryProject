
# some imports
from Book import Book
from Person import Client,Librarian
from BorrowingOrder import Borrowing
# Press the green button in the gutter to run the script.

book1 = Book("Biology","Basic Concepts of Biology", "Jerry McKarvy")
Lib1 =  Librarian("Amma Wasntion" , 40, "Full")
# book2 = Book("Physics","Basic Concepts of Physics", "Lus Norman")
Lib2 =  Librarian("Jakson Welly" , 43, "Part")
# book3 = Book("Mathematics","Basic Concepts of Mathmatics", "Welly Anderson")
Librarians = [Lib1, Lib2]
# book4 = Book("Statics","Basic Concepts of Statics", "Kael Hexson")
# book5 = Book("Science","Basic Concepts of Science", "Martha Lue")

# CL1 = Client("cl001", "Nelly Ln", 30, "00594xxxx")
# CL2 = Client("cl002", "Susie", 28, "00893xxxx")
# CL3 = Client("cl003", "Zak", 32, "00674xxxx")
# CL4 = Client("cl004", "Sally", 38, "00594xxxx")=
# CL5 = Client("cl001", "Philip", 33, "00098xxx")



# Lists of objects
Books = [book1]
Clients = []
BorrowingOrders= []

#To make change
def change_book_status (id):
    for book in Books:
        if id == book.get_bookid():
            book.setstatus("Active")

def get_client( idCL):
    for cl in Clients:
        if cl.getId() == idCL:
            return cl

i = True
while i :
    client = None
    choice = int(input("Welcome, our services are: "
                       "\n1.List available books"
                       "\n2.Borrow a book"
                       "\n3.Return book(s)"
                       "\n4.List borrowed books"
                       "\n Please Press 0 to exist."
                       "\n\n Enter Number:"))
    if choice == 1:
        if len(Books) == 0:
            print("There is no books available")
        else:
            for book in Books:
                if book.get_status() == "Active":
                    print(book.get_book_detials())

    elif choice == 2:
        flag = int(input("1.New Client\n2.Current Client\n\n Enter Number:"))
        if flag == 1:
            name = str(input("Your Name"))
            age = int(input("Your Age"))
            phone = str(input("Your Phone No."))
            client =  Client(name= name, age= age, phone= phone)
            #add to clients list
            Clients.append(client)
            print("You have added to our current clients successfully")
            flag = 2

        if flag == 2:
            for book in Books:
                print(book.get_book_detials())
            book_id = str(input("Please enter The Book Id that you want to borrow."))
            client_id = str(input("Please enter  Client ID."))
            if book_id == book.get_bookid():
                for client in Clients:
                    if client_id == client.getId():
                        order = Borrowing(client,book)
                        #add to orders list
                        BorrowingOrders.append(order)
                        book.setstatus("Inactive")
                        print("You have borrowed the book with ID %s successfully"%book_id)
            else:
                print("There is No such ID: %s found, Try again"%book_id)

    elif choice == 3:
        book_id2 = str(input("Please enter the Book ID that you have borrowed"))
        for order in BorrowingOrders:
            if book_id2 == order.get_borrowed_book_id():
                duration = str(order.get_end_date().date() - order.get_init_date())
                if duration == '10':
                    order.set_status("Expired")
                    change_book_status(book_id2)
                    print("You have returned the Book with ID: %s successfully" % book_id2)
                else:
                    order.set_status("Canceled")
                    change_book_status(book_id2)
                    print("You have returned the Book with ID: %s successfully" % book_id2)

    elif choice == 4:
        pang = int(input("1.Active borrowed book(s)\n2.Expired borrowed book(s)\n3.Canceled borrowed book(s)"))
        for borrowed in BorrowingOrders:
            if pang == 1 and borrowed.get_order_status() == "Active":
                print(borrowed.get_order_details())
            elif pang == 2 and borrowed.get_order_status() == "Expired":
                print(borrowed.get_order_details())
            elif pang ==3 and borrowed.get_order_status() == "Canceled":
                print(borrowed.get_order_details())

    elif choice == 0:
        i = False








