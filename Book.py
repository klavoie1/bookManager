class Book:
    def __init__(self, title, author, publish_date, genre, page_count):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.genre = genre
        self.page_count = page_count

    def show_title(self):
        return self.title

    def print_details(self):
        print(f"\nBook Information\n",
              f"The Title: {self.title}\n",
              f"The Author: {self.author}\n",
              f"The Date First Published: {self.publish_date}\n",
              f"The Genre(s): {self.genre}\n",
              f"The number of Pages: {self.page_count}\n")