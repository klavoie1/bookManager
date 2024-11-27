from PyQt5 import QtWidgets, QtGui
import json
from Book import Book
class Main_Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Sample book data
        self.books = self.load_from_json("bookDetails.json")
        # Create the layout
        layout = QtWidgets.QVBoxLayout()

        # Search bar
        self.search_bar = QtWidgets.QLineEdit(self)
        self.search_bar.setPlaceholderText("Search books or Authors...")
        self.search_bar.textChanged.connect(self.perform_search)
        layout.addWidget(self.search_bar)

        # ListWidget to display search results
        self.search_results_list = QtWidgets.QListWidget()
        layout.addWidget(self.search_results_list)

        # Populate the list with book titles
        for book in self.books:
            self.search_results_list.addItem(book.get_title)


        # Connect itemClicked signal to show book details
        self.search_results_list.itemClicked.connect(self.show_book_details)

        # Set the layout
        self.setLayout(layout)

    def show_book_details(self, item):
        """Handle the click on a book item and show its details."""
        clicked_title = item.text()
        selected_book = None
        for book in self.books:
            if book.get_title == clicked_title:
                selected_book = book
                break

        if selected_book:
            details_dialog = BookDetailsDialog(selected_book)
            details_dialog.exec_()

    def perform_search(self):
        """Perform a search and update the results list."""
        query = self.search_bar.text().lower()  # Get the text in the search bar
        self.search_results_list.clear()  # Clear the current list

        # Filter books based on query, search through title and author
        filtered_books = [
            book for book in self.books if query in book.get_title.lower() or query in book.get_author.lower()
        ]

        # Add filtered book titles to the list
        for book in filtered_books:
            self.search_results_list.addItem(book.get_title)


    def load_from_json(self, jsonfile):
        """loads the Book JSON file"""
        try:
            with open(jsonfile, "r") as file:
                data = json.load(file)
                return [Book.from_json(book_data) for book_data in data]
        except FileNotFoundError:
            return [] # returns as empty list of no file is found
        except json.JSONDecodeError:
            return [] # returns error if there is an error in decoding the JSON file

    def save_books_to_json(self, jsonfile):
        """Save books to a JSON file."""
        with open(jsonfile, "w") as file:
            data = [Book.to_dict_details(book) for book in self.books]
            json.dump(data, file, indent=4)

    def show_book_details(self, item):
        """Handle the click on a book item and show its details."""
        # Find the clicked book based on the title
        clicked_title = item.text()
        selected_book = None
        for book in self.books:
            if book._title == clicked_title:
                selected_book = book
                break
        
        if selected_book:
            # Create a dialog or a new widget to show the details of the selected book
            details_dialog = BookDetailsDialog(selected_book)
            details_dialog.exec_()


class BookDetailsDialog(QtWidgets.QDialog):
    def __init__(self, book):
        super().__init__()

        self.setWindowTitle(f"Details for {book.get_title}")

        layout = QtWidgets.QVBoxLayout()

        book_details = book.get_details()

        # Add book details to the layout
        for key, value in book_details.items():
            label = QtWidgets.QLabel(f"{key}: {value}")
            label.setFont(QtGui.QFont("Arial", 12))
            layout.addWidget(label)

        close_button = QtWidgets.QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

