class Book: 
    def __init__(self, title, genre, author, completed = False, id = None):
        self.title = title
        self.genre = genre
        self.author = author
        self.completed = completed
        self.id = id


    def mark_completed(self):
        self.completed = True