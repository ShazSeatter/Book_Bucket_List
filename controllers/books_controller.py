from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

# RESTful CRUD routes

# INDEX
# GET - homepage '/'

# !!!!!!!! this will need to be changed later - for the purpose of making sure it works
# @books_blueprint.route('/')
# def book():
#     books = book_repository.