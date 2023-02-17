from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository 


def save(book):
    sql = "INSERT INTO books (title, author_id, completed) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book