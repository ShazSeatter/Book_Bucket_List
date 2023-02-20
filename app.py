from flask import Flask, render_template
from controllers.books_controller import books_blueprint
from controllers.authors_controller import authors_blueprint
from models.book import Book

import repositories.book_repository as book_repository 

app = Flask(__name__)
app.register_blueprint(books_blueprint)
app.register_blueprint(authors_blueprint)



@app.route('/')
def home():
    book = book_repository.select_all
    return render_template('index.html', title = "Home")

if __name__ == '__main__':
    app.run(debug=True)
