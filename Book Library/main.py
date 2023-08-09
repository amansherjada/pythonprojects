class Library:

  def __init__(self, no_of_books):
    self.no_of_books = no_of_books
    self.books = []

  def add_book(self, book):
    self.books.append(book)

  def get_number_of_books(self):
    return len(self.books)

  def print_all_books(self):
    print("Books in the library:")
    for book in self.books:
      print("- " + book)


# Creating a library and performing operations
def main():
  my_library = Library(no_of_books=100)

  my_library.add_book("Python Programming")
  my_library.add_book("Introduction to Algorithms")
  my_library.add_book("The Great Gatsby")
  my_library.add_book("Harry Potter and the Sorcerer's Stone")

  print("Number of books in the library:", my_library.get_number_of_books())
  my_library.print_all_books()

  print("Adding a new book...")
  my_library.add_book("Data Science Handbook")

  print("Number of books in the library:", my_library.get_number_of_books())
  my_library.print_all_books()


if __name__ == "__main__":
  main()
