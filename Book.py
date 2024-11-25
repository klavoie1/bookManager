class Book:
    def __init__(self, title, author, publish_date, genre, page_count):
        self._title = title
        self._author = author
        self._publish_date = publish_date
        self._genre = genre
        self._page_count = page_count


    # Title Getter
    @property
    def get_title(self):
        return self._title
    
    # Title Setter 
    @get_title.setter
    def set_title(self, new_title):
        if not new_title:
            raise ValueError("Title cannot be Empty!")
        self._title = new_title
    
    # Author Getter
    @property
    def get_author(self):
        return self._author
    
    # Author Setter
    @get_author.setter
    def set_author(self, new_author):
        if not new_author:
            raise ValueError("Author cannot be Empty!")
        self._title = new_author
    
    # Publish Date Getter
    @property
    def get_publish_date(self):
        return self._publish_date
    
    # Publish Date Setter
    @get_publish_date.setter
    def set_publish_date(self, new_publish_date):
        if not new_publish_date:
            raise ValueError("Publish Date cannot be Empty!")
        self._title = new_publish_date

    # Genre Getter
    @property
    def get_genre(self):
        return self._genre
    
    # Genre Setter 
    @get_genre.setter
    def set_genre(self, new_genre):
        if not new_genre:
            raise ValueError("Genre cannot be Empty!")
        self._title = new_genre

    # Page Count Getter
    @property
    def get_page_count(self):
        return self._page_count
    
    # Page Count Setter
    @get_page_count.setter
    def set_page_count(self, new_page_count):
        if not new_page_count:
            raise ValueError("Page Count cannot be Empty!")
        self._page_count
    

    def get_details(self):
        """Return a dictionary of the books details"""
        return {
            "Title": self._title,
            "Author": self._author,
            "Year": self._publish_date,
            "Genre": self._genre,
            "Pages": self._page_count
        }