from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository 

def save(book):
    sql = "INSERT INTO books (title, author_id, completed, notes) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.completed, book.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['completed'], row['notes'], row['id'])
        books.append(book)
    return books


def select_all_finished():
    finished_books =[]

    sql = "SELECT * FROM books WHERE completed = %s"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['completed'], row['notes'], row['id'])
        finished_books.append(book)
    return finished_books

def select_all_tbr():
    tbr_books =[]

    sql = "SELECT * FROM books WHERE completed = %s"
    values = [False]
    results = run_sql(sql, values)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['completed'], row['notes'], row['id'])
        tbr_books.append(book)

    return tbr_books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['completed'], result['notes'], result['id'])

    return book 


# review
def update(book):
    sql = "UPDATE books SET (title, author_id, completed, notes) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.completed, book.notes, book.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)