import pdb
from models.book import Book 
from models.author import Author 

import repositories.book_repository as book_repository 
import repositories.author_repository as author_repository

# AUTHOR 1 - DUMMY DATA
author_1 = Author("Adam", "Kay")
author_repository.save(author_1)

# AUTHOR 2 - DUMMY DATA
author_2 = Author("Lucy", "Score")
author_repository.save(author_2)

# BOOK 1 - DUMMY DATA
book_1 = Book("Undoctored", author_1)
book_repository.save(book_1)

# BOOK 2 - DUMMY DATA
book_2 = Book("Things We Hide From The Light", author_2)
book_repository.save(book_2)
