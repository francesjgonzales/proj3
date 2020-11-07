from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import pymongo


load_dotenv()


MONGO_URL = os.environ.get('MONGO_URL')
DB_NAME = "student_tracker"


client = pymongo.MongoClient(MONGO_URL)
db = client['student_tracker']


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


# READ

@app.route('/students')
def show_students():
    all_students = db.students.find()
    return render_template('all_students.template.html',
                           all_students=all_students)


@app.route('/teachers')
def show_teachers():
    all_teachers = db.teachers.find()
    print(all_teachers)
    return render_template('teachers.template.html')


# CREATE

@app.route('/students/create')
def show_create_student():
    return render_template('create_student.template.html')


@app.route('/students/create', methods=["POST"])
def process_create_animal():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    date_of_birth = int(request.form.get("date_of_birth"))

    new_record = {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth
    }

    db.students.insert_one(new_record)
    return redirect(url_for('show_students'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
