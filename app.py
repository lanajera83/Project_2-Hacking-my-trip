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

import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/flights_data.sqlite"
db = SQLAlchemy(app)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
Samples_Metadata = Base.classes.sample_metadata
Samples = Base.classes.samples


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
    return render_template("results.html", p_from=p_from, p_to=p_to, p_date=p_date)



if __name__ == "__main__":
    app.run(debug=True)
