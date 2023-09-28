from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# create the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    new_book = Books(id= 1, title= "5 am Club", author= "Robin Sharma", rating= 9.3)
    db.session.add(new_book)
    db.session.commit()


# if __name__ == '__main__':
#     app.run(debug=True)