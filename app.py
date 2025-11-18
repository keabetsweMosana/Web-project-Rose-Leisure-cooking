from flask import Flask, render_template, redirect, request
import sqlite3 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/bookings")
def bookings():
    return render_template("bookings.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/login")
def login():
    return render_template("login.html")

def create_table():
    con = sqlite3.connect('forms.db')
    c = con.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS data(
            email TEXT NOT NULL UNIQUE,
            message TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")

        if email and message:
            con = sqlite3.connect('forms.db')
            c = con.cursor()
            c.execute("INSERT INTO data (email, message) VALUES (?, ?)", (email, message))
            con.commit()
            con.close()
            return render_template("thanks.html")
    return render_template("contact.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

if __name__ == "__main__":
    create_table()
    app.run(debug=True)


