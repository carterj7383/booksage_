import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask App
app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = 'supersecretkey'  # Change this to a secure key in production

# Debugging template directory
print("Current Working Directory:", os.getcwd())
print("Templates Folder Exists:", os.path.exists("templates"))
print("mainPage.html Exists:", os.path.exists("templates/mainPage.html"))

# Database Connection Helper Function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enables column access by name
    return conn

# Home Page (Main Page)
@app.route('/')
def index():
    return render_template('mainPage.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session['user_id'] = user["id"]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='scrypt')

        conn = get_db_connection()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
                      (first_name, last_name, email, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))
        finally:
            conn.close()

    return render_template('register.html')

# Profile Route
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT first_name, last_name, email FROM users WHERE id = ?", (session['user_id'],))
    user = c.fetchone()
    conn.close()

    return render_template('profile.html', user=user)

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT first_name, last_name, email FROM users WHERE id = ?", (session['user_id'],))
    user = c.fetchone()
    conn.close()

    return render_template('dashboard.html', user=user)

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
