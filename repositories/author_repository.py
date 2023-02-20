from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results  = run_sql(sql, values)
    id = results[0]['id']
    author.id = id

    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'] )
        authors.append(author)
    return authors


def update(author):
    sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [author.first_name, author.last_name, author.id]
    run_sql(sql, values)


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = Author(result['first_name'], result['last_name'], result['id'])
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

