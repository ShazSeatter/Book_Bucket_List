from flask import Flask, render_template, request, redirect

from models.book import Book
from models.author import Author

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
    return render_template('books/index.html', all_books = books)

# CRUD FUNCTIONALITY FOR CREATING NEW AUTHOR 

# # NEW
# # GET 'author/new'
# @books_blueprint.route('/books/authors/new')
# def new_author():
#     authors = author_repository.select_all()
#     return render_template('authors/new.html', all_authors = authors)


# # CREATE
# # POST '/books'
# @books_blueprint.route('/books', methods=['POST'])
# def create_author():
#    first_name = request.form['first-name']
#    last_name = request.form['last-name']
#    author = Author(first_name, last_name)
#    author_repository.save(author)
#    return redirect('/books')



# NEW BOOK

# NEW
# GET 'books/new'
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author = author_repository.select(request.form['author_id'])
    book = Book(title, author)
    book_repository.save(book)
    return redirect('/books')