#SPEACIAL METHODS

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #makes it legible when you call a string method on book
    def __str__(self):
        return f"Title: {self.title}, Auhtor: {self.author}, Page: {self.pages}"

    #allows you to see the length of an OBJECT
    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book has been destroyed")

b = Book("Python", "Monty", 500)
print(b)
print(len(b))
#this will delete the book in question 
del b
