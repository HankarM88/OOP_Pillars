class Library:
    def __init__(self,books,name):
        self.name=name
        self.books=books

    def display_books(self):
        print(f'Available Books in {self.name} Library:\n')
        for book in self.books:
            print(book)

    def add_book(self,returned_book):
        self.books.append(returned_book)
        print(f'You have returned {returned_book}. Thank you!')

    def lend_book(self,requested_book):
        if requested_book in self.books:
            self.books.remove(requested_book)
        else:
            print('This Book is Not Available in the Library !')

class Student:
    def __init__(self, name,ID,age):
        self.name=name
        self.id=ID
        self.age=age

    def request_book(self):
        self.book=input('Type the name of a book you want to borrow:\n')
        print(f'You have requesetd : {self.book}')


    def return_book(self):
        self.book=input('type the Name of the book you want to return ?:')
        return self.book

def main():

    #instanciate the classes
    list_books=["The outsider","Zara","Ecco hummo","The Double",
    "Master data science","The world as will and presentation"]
    lib=Library(list_books,'Al Farabi')
    st=Student('H.M',103,32)
    while True:
        choice=int(input('Type:\n1:Display availaibale Books\n2:Request a Book\n3:Return a Book\n4:Exit\n'))
        if choice==2:
            requested_book=st.request_book()
            lib.lend_book(requested_book)
        elif choice==3:
            returned_book= st.return_book()
            lib.add_book(returned_book)
        elif choice==1:
            lib.display_books()
        else:
            break
# main the process
if __name__ == '__main__':
    main()
