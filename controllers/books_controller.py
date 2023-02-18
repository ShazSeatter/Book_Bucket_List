from flask import Flask, render_template, request, redirect

from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD routes

# INDEX
# GET - homepage '/'

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('test.html', all_books = books)
