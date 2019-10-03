from sqlalchemy import func
from flask_pymongo import PyMongo
from forms import SearchForm
import scrape_flights
import pymongo

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/flights_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# Route that will trigger the scrape function
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        p_from = request.form["desde"]
        p_to = request.form["hasta"]
        p_date = request.form["fecha"]
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
