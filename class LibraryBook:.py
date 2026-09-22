class LibraryBook:
    # Class variable
    total_books = 0

    def _init_(self, book_id, title, author):
        self.book_id = book_id
        self._title = title
        self.author = author

        # Increase total books whenever a book is created
        LibraryBook.total_books += 1

    # -----------------------------
    # GETTER METHOD
    # -----------------------------
    @property
    def title(self):
        return self._title

    # -----------------------------
    # SETTER METHOD
    # -----------------------------
    @title.setter
    def title(self, new_title):
        if new_title.strip() == "":
            print("Book title cannot be empty.")
        else:
            self._title = new_title

    # -----------------------------
    # CLASS METHOD
    # -----------------------------
    @classmethod
    def get_total_books(cls):
        return cls.total_books

    # -----------------------------
    # STATIC METHOD
    # -----------------------------
    @staticmethod
    def valid_book_id(book_id):
        return book_id.startswith("BK") and len(book_id) == 5

    # Display book information
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("------------------------")


# =================================
# LIBRARY MANAGEMENT SYSTEM
# =================================

print("===== LIBRARY MANAGEMENT SYSTEM =====")

# Creating books
book1 = LibraryBook("BK001", "Introduction to Python", "John Smith")
book2 = LibraryBook("BK002", "Database Systems", "Mary Jones")

# Display books
print("\nBOOK 1")
book1.display_book()

print("BOOK 2")
book2.display_book()

# =================================
# USING GETTER
# =================================

print("Current title of Book 1:", book1.title)

# =================================
# USING SETTER
# =================================

book1.title = "Advanced Python Programming"

print("Updated title of Book 1:", book1.title)
# =================================
# USING CLASS METHOD
# =================================
print("\nTotal books in library:",
      LibraryBook.get_total_books())
# =================================
# USING STATIC METHOD
# =================================
print("\nChecking Book IDs:")

print("BK001:", LibraryBook.valid_book_id("BK001"))
print("12345:", LibraryBook.valid_book_id("12345"))

print("\n===== PROGRAM COMPLETED =====")