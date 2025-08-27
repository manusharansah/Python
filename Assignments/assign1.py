'''
A Library Managemnet System
Core Topics:
->Classes/Objects
->Inheritance
->Iterators
->Polymorphism
->pop() usage
->Scope (global/nonlocal/local)
'''




class Book():
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class User():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.borrowed = []
    
class Student(User):
    def role(self):
        print("Student")
class Teacher(User):
    def role(self):
        print('Teacher')

class Library():
    def __init__(self):
        self.Books = []
    def add_book(self,new_book):
        global total_books
        self.Books.append(new_book)
        total_books +=1
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if(self.i < len(self.Books)):
            b = self.Books[self.i]
            self.i += 1 
            return b
        else:
            raise StopIteration
    def remove_book(self):
        global total_books
        self.Books.pop()
        total_books -= 1
    def borrow_book(self,book,user):
        global total_books
        if self.search_book(book.title):
            for x in self.Books:
                if book.title == x.title:
                    borrowed_book = x
                    break
            self.Books.remove(x)
            total_books -=1
        user.borrowed.append(borrowed_book)
    def search_book(self,book_title):
        for x in self.Books:
            if book_title == x.title:
                return True
        return False
    def return_book(self,user,book):
        global total_books
        for x in user.borrowed:
            if book.title == x.title:
                user.borrowed.remove(book)
                total_books+=1
                self.Books.append(book)
            
        
def print_role(user):
    user.role()

total_books = 0



lib = Library()


lib.add_book(Book("Python 101", "Guido", 1991))
lib.add_book(Book("Learning AI", "Andrew", 2018))


for b in lib:
    print(b)


lib.remove_book()


s = Student("Manu", 21)
t = Teacher("Sharan", 35)

print_role(s)  
print_role(t)  


print("Total books in system:", total_books)
