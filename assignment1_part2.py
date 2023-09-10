
# Define the Book class
class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")

# Create two instances of the Book class
book1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
book2 = Book("Walter Scott", "Ivanhoe: A Romance")

# Display the information of both books
book1.display()
book2.display()
