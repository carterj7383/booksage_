from flask import Flask, render_template, redirect, url_for, request, session, flash
import sqlite3
import os
import sys
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from functools import lru_cache

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = Flask(__name__, 
            template_folder=resource_path('templates'),
            static_folder=resource_path('static'))
app.secret_key = 'your_secret_key'

@lru_cache(maxsize=100)
def get_book_cover(isbn=None, title=None, author=None):
    if isbn:
        isbn = str(isbn).strip().replace('-', '')
        open_library_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"
        
        try:
            response = requests.head(open_library_url)
            if response.status_code == 200:
                return open_library_url
        except:
            pass
    
    if title or author:
        try:
            query_parts = []
            if title:
                query_parts.append(f"intitle:{title}")
            if author:
                query_parts.append(f"inauthor:{author}")
            
            query = "+".join(query_parts)
            google_books_url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=1"
            
            response = requests.get(google_books_url, timeout=5)
            if response.status_code != 200:
                return url_for('static', filename='images/default-book-cover.svg')
                
            data = response.json()
            
            if data.get('items') and data['items'][0].get('volumeInfo'):
                image_links = data['items'][0]['volumeInfo'].get('imageLinks', {})
                
                for img_size in ['large', 'medium', 'small', 'thumbnail', 'smallThumbnail']:
                    if img_size in image_links:
                        image_url = image_links[img_size].replace('http:', 'https:')
                        image_url = image_url.split('&zoom=')[0]
                        return image_url
                        
        except Exception as e:
            print(f"Google Books API error: {e}")
    
    return url_for('static', filename='images/default-book-cover.svg')

app.jinja_env.globals.update(get_book_cover=get_book_cover)

def get_db_connection():
    conn = sqlite3.connect(resource_path('database.db'))
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    recommended_books = [
        {
            'title': 'The Algorithm Design Manual',
            'author': 'Steven S. Skiena',
            'isbn': '9781849967204',
            'rating': 4.5,
            'reviews': 128
        },
        {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'isbn': '9780132350884',
            'rating': 4.8,
            'reviews': 256
        },
        {
            'title': 'Data Science for Business',
            'author': 'Foster Provost',
            'isbn': '9781449361327',
            'rating': 4.3,
            'reviews': 89
        },
        {
            'title': 'Hands-On Machine Learning',
            'author': 'Aurélien Géron',
            'isbn': '9781492032649',
            'rating': 4.6,
            'reviews': 167
        }
    ]
    
    return render_template('mainPage.html', recommended_books=recommended_books)

@app.route('/browse')
def browse():
    browse_books = [
        {
            'title': 'Algorithms Unlocked',
            'author': 'Thomas H. Cormen',
            'isbn': '9780262033848',
            'rating': 4.5,
            'reviews': 86,
            'description': 'An accessible introduction to algorithms that provides explanations of fundamental concepts alongside practical examples.',
            'year': 2013,
            'pages': 242
        },
        {
            'title': 'Deep Learning with Python',
            'author': 'François Chollet',
            'isbn': '9781617295978',
            'rating': 4.8,
            'reviews': 124,
            'description': 'Written by the creator of Keras, this book provides a practical introduction to deep learning with Python and TensorFlow.',
            'year': 2021,
            'pages': 504
        },
        {
            'title': 'The Pragmatic Programmer',
            'author': 'Andrew Hunt, David Thomas',
            'isbn': '9780135957059',
            'rating': 4.6,
            'reviews': 192,
            'description': 'A classic guide to software craftsmanship that offers practical advice for improving the development process in a pragmatic, impactful way.',
            'year': 2019,
            'pages': 352
        },
        {
            'title': 'Database Systems: The Complete Book',
            'author': 'Hector Garcia-Molina, Jeffrey D. Ullman, Jennifer Widom',
            'isbn': '9780131873254',
            'rating': 4.3,
            'reviews': 104,
            'description': 'A comprehensive introduction to modern database systems, covering everything from database design to query optimization and transaction management.',
            'year': 2008,
            'pages': 1152
        },
        {
            'title': 'Structure and Interpretation of Computer Programs',
            'author': 'Harold Abelson, Gerald Jay Sussman',
            'isbn': '9780262510875',
            'rating': 4.7,
            'reviews': 213,
            'description': 'A classic computer science textbook that teaches fundamental principles of programming using Scheme. Known for its philosophical approach to programming.',
            'year': 1996,
            'pages': 456
        }
    ]
    
    return render_template('browse.html', books=browse_books)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['email'] = user['email']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = generate_password_hash(password)
        
        conn = get_db_connection()
        existing_user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        
        if existing_user:
            flash('Email already exists. Please choose a different one.')
            conn.close()
            return redirect(url_for('register'))
        
        conn.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)',
                     (first_name, last_name, email, hashed_password))
        conn.commit()
        conn.close()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    user = conn.execute('SELECT first_name, last_name FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    conn.close()
    
    return render_template('dashboard.html', user=user)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    user = conn.execute('SELECT first_name, last_name, email FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    conn.close()
    
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

init_db()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)