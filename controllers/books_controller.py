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
    completed = True if 'completed' in request.form else False
    book = Book(title, author, completed)
    book_repository.save(book)
    return redirect('/books')

# SHOW
# GET '/books/<id>
@books_blueprint.route('/books/<id>/show')
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)


# EDIT
# GET 'books/<id>/edit'
@books_blueprint.route('/books/<id>/edit')
def edit_books(id):
    authors = author_repository.select_all()
    book = book_repository.select(id)
    return render_template('/books/edit.html', all_authors = authors, book = book)

# UPDATE
@books_blueprint.route('/books/<id>', methods=["POST"])
def update_book(id):
    title = request.form['title']
    author_id = request.form['author_id']
    completed = request.form['completed']
    author = author_repository.select(author_id)
    book = Book(title, author, completed, id)
    book_repository.update(book)
    return redirect('/books')


# DELETE
@books_blueprint.route('/books/<id>/delete', methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
