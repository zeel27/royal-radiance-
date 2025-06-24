from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- Database Connection Helper ---
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- Home Page ---
@app.route('/')
def home():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('index.html', products=products)

# --- Category Pages ---
@app.route('/category/<string:category>')
def category(category):
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products WHERE category = ?', (category.title(),)).fetchall()
    conn.close()
    return render_template('category.html', category=category.title(), products=products)

# --- Contact Form ---
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        conn = get_db_connection()
        conn.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
        conn.close()
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return '<h1>Thank you for contacting us!</h1>'

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
