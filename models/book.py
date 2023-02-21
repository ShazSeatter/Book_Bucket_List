class Book: 
    def __init__(self, title, author, completed = False, review = None, id = None):
        self.title = title
        self.author = author
        self.completed = completed
        self.review = review
        self.id = id

    def mark_completed(self, completed):
        self.completed = completed

