from flask import Flask, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()


MONGO_URL = os.environ.get('MONGO_URL')
DB_NAME = "student_attendance"

client = pymongo.MongoClient(MONGO_URL)
db = client['student_attendance']


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def home():
    return render_template('home.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
