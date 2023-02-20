class Book: 
    def __init__(self, title, author, completed = False,  id = None):
        self.title = title
        self.author = author
        self.completed = completed
        self.id = id

    def mark_completed(self, completed):
        self.completed = completed

