from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "I am from india"
@app.route("/phone")
def lwphone():
	retuen "7888562334"

app.run(host="0.0.0.0")