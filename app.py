from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def Login():
    return render_template("login.html")

@app.route("/home")
def Login():
    return render_template("login.html")

app.run(debug=True)