from flask import Flask, render_template
from flask_cors import CORS


app = Flask(_name_)
CORS(app)



@app.route("/")
def ibm():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/report")
def report():
    return render_template("report.html")

if _name_ == "_main_":
   app.run(debug=True)