from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="DemoHosting",
        user="postgres",
        password="riddhi1826"
    )


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    if user:
        return render_template("dashboard.html")
    else:
        return " Invalid Login"


if __name__ == "__main__":
    app.run(debug=True)
