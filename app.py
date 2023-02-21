from flask import Flask, render_template
from controllers.books_controller import books_blueprint
from controllers.authors_controller import authors_blueprint

import repositories.book_repository as book_repository

app = Flask(__name__)

app.register_blueprint(books_blueprint)
app.register_blueprint(authors_blueprint)



@app.route('/')
def home():
    true_book = book_repository.select_all_finished()
    false_book = book_repository.select_all_tbr()
    return render_template('index.html', title = "Home", all_true_books = true_book, all_false_books = false_book)


if __name__ == '__main__':
    app.run(debug=True)
