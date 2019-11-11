from bottle import get, post, request, run, static_file
import hashlib
import sqlite3

@get("/")
def login_page():
	return static_file("index.html", root="")

@post("/login")
def login():
	conn = sqlite3.connect("users.db")
	c = conn.cursor()
	hashed_password = hashlib.sha256()
	
	username = request.forms.get("username")
	password = request.forms.get("password")
	hashed_password.update(bytes(password, "utf-8"))
	
	c.execute("SELECT * FROM users WHERE username = ?", (username,))
	
	if hashed_password.digest() == c.fetchone()[1]:
		return "<p>Yay</p>"
	else:
		return "<p>No</p>"
	
	conn.commit()
	conn.close()

run(host="localhost", port=8080, debug=True)
