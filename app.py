from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="book_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        query = "INSERT INTO books (title, author) VALUES (%s, %s)"
        cursor.execute(query, (title, author))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/view_books',methods=['GET'])
def view_books():
    query = "SELECT title, author FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    return render_template('view_books.html', books=books)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)
