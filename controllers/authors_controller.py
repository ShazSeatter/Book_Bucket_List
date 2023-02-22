from flask import Flask, render_template, request, redirect
from models.author import Author

import string
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

from flask import Blueprint

authors_blueprint = Blueprint("authors", __name__)



@authors_blueprint.route('/authors')
def authors():
    authors = author_repository.select_all()
    list_books = author_repository.books
    return render_template('authors/index.html', list_books = list_books, title = "Authors", all_authors = authors)


# CRUD FUNCTIONALITY FOR CREATING NEW AUTHOR 

# # NEW
# # GET 'author/new'
@authors_blueprint.route('/authors/new')
def new_author():
    authors = author_repository.select_all()
    return render_template('authors/new.html', title = "Add Author", all_authors = authors)


# CREATE
# POST '/books'
@authors_blueprint.route('/authors', methods=['POST'])
def create_author():
   first_name = request.form['first-name']
   last_name = request.form['last-name']
   cap_first = string.capwords(first_name)
   cap_last = string.capwords(last_name)
   author = Author(cap_first, cap_last)
   author_repository.save(author)
   return redirect('/authors')


# EDIT
# GET 'authors/<id>/edit'
@authors_blueprint.route('/authors/<id>/edit')
def edit_authors(id):
    author = author_repository.select(id)
    return render_template('/authors/edit.html', title = "Edit Author", author = author)

# UPDATE
# POST '/authors/<id>'
@authors_blueprint.route('/authors/<id>', methods=["POST"])
def update_author(id):
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    cap_first = string.capwords(first_name)
    cap_last = string.capwords(last_name)
    author = Author(cap_first, cap_last, id)
    author_repository.update(author)
    return redirect('/authors')


# DELETE
@authors_blueprint.route('/authors/<id>/delete', methods=["POST"])
def delete_author(id):
    author_repository.delete(id)
    return redirect('/authors')
    # # books_with_author = author_repository.books(author)
    # author_empty = author_repository.delete(id) # this will automatically delete an author with no book, 
    # # does not delete authors with books
    # authors_with_books = author_repository.books(author)
    # return render_template('authors/index.html', authors_with_books = authors_with_books)
    # return redirect('/authors')
    # # return render_template('authors/index.html', books_author = books_with_author, author_empty = author_empty)