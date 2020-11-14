from flask import Flask, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import pymongo
import datetime


load_dotenv()

app = Flask(__name__)

MONGO_URL = os.environ.get('MONGO_URL')
DB_NAME = "student_tracker"
SECRET_KEY = os.environ.get('SECRET_KEY')

# CONNECT TO MONGODB
client = pymongo.MongoClient(MONGO_URL)
db = client['student_tracker']

# SET UP SECRET KEY TO FLASK APP
app.secret_key = os.environ.get('SECRET_KEY')


# SET UP DATE AND TIME

currentDate = datetime.datetime.now()


# HOME

@app.route('/')
def home():
    return render_template('home.template.html')


# TEACHER SIGN UP
@app.route('/teachers/signup')
def show_create_teacher():
    return render_template('teachers/create_teacher.template.html')


@app.route('/teachers/signup', methods=["POST"])
def process_create_teacher():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    if len(first_name) == 0:
        flash("Name cannot be empty", "error")
        return redirect(url_for('show_create_teacher'))

    new_record = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        'password': password
    }

    db.teachers.insert_one(new_record)
    flash("Sign up successful")
    return redirect(url_for('show_teacher_main'))


# TEACHER LOGIN

@app.route('/teachers/login')
def teacher_login():
    return render_template('teachers/login_teacher.template.html')


@app.route('/teachers/login', methods=["POST"])
def process_teacher_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if len(email) == 0:
        flash("Please fill up email", "error")
        return redirect(url_for('teacher_login'))

    else:
        db.teachers.find_one({
            'email': email,
            'password': password
        })
    return redirect(url_for("show_teachers"))


# TEACHERS LIST

@app.route('/teachers')
def show_teachers():
    all_teachers = db.teachers.find()
    return render_template('teachers/all_teachers.template.html',
                           all_teachers=all_teachers)


# TEACHER WELCOME PAGE

@app.route('/teachers/main')
def show_teacher_main():
    return render_template('teachers/teacher_main.template.html')


# STUDENT PROFILE

@app.route('/students')
def show_students():
    all_students = db.students.find()
    return render_template('students/all_students.template.html',
                           all_students=all_students)


# STUDENT ATTENDANCE PAGE

@app.route('/attendance')
def show_attendance():
    all_attendance = db.attendance.find()
    all_students = db.students.find()
    return render_template('attendance/all_attendance.template.html',
                           all_attendance=all_attendance,
                           all_students=all_students)


# CREATE STUDENT ATTENDANCE PAGE

@app.route('/attendance/create')
def show_create_attendance():
    return render_template('attendance/create_attendance.template.html')


@app.route('/attendance/create', methods=["POST"])
def process_create_attendance():
    clock_in = request.form.get("clock_in")
    clock_out = request.form.get("clock_out")
    temparature = request.form.get("temparature")
    isPresent = request.form.get("isPresent")

    new_record = {
        "clock_in": clock_in,
        "clock_out": clock_out,
        "temparature": temparature,
        "isPresent": isPresent
    }

    db.attendance.insert_one(new_record)
    return redirect(url_for('show_create_attendance'))


# PARENTS MAIN PAGE

@app.route('/parents')
def show_parents():
    all_parents = db.parents.find()
    return render_template('parents/all_parents.template.html',
                           all_parents=all_parents)


# PARENT SIGN UP

@app.route('/parents/signup')
def show_create_parent():
    return render_template('parents/create_parent.template.html')


@app.route('/parents/signup', methods=["POST"])
def process_create_parent():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    if len(first_name) == 0:
        flash("Name cannot be empty", "error")
        return redirect(url_for('show_create_parent'))

    new_record = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        'password': password
    }

    db.parents.insert_one(new_record)
    flash("Sign up successful")
    return redirect(url_for('show_parents'))


# PARENT LOGIN

@app.route('/parents/login')
def parent_login():
    return render_template('parents/login_parent.template.html')


@app.route('/parents/login', methods=["POST", "GET"])
def process_parents_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if len(email) == 0:
        flash("Name cannot be empty", "error")
        return redirect(url_for('teacher_login'))

    db.teachers.find_one({
        'email': email,
        'password': password
    })
    return redirect(url_for("show_parents"))


# CREATE STUDENT PROFILE

@app.route('/students/create')
def show_create_student():
    return render_template('students/create_student.template.html')


@app.route('/students/create', methods=["POST"])
def process_create_student():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    date_of_birth = request.form.get("date_of_birth")
    class_groupId = request.form.get("class_groupId")

    new_record = {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "class_groupId": class_groupId
    }

    db.students.insert_one(new_record)
    return redirect(url_for('show_students'))


# UPDATE STUDENT AND TEACHER PROFILE

@app.route('/students/edit/<student_id>')
def show_edit_student(student_id):
    student = db.students.find_one({
        '_id': ObjectId(student_id)
    })
    return render_template('students/edit_student.template.html',
                           student=student)


@app.route('/students/edit/<student_id>', methods=["POST"])
def process_edit_student(student_id):
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    date_of_birth = request.form.get("date_of_birth")

    db.students.update_one({
        "_id": ObjectId(student_id)
    }, {
        "$set": {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth
        }
    })
    return redirect(url_for('show_students'))


@app.route('/teachers/edit/<teacher_id>')
def show_edit_teacher(teacher_id):
    teacher = db.teachers.find_one({
        '_id': ObjectId(teacher_id)
    })
    return render_template('teachers/edit_teacher.template.html',
                           teacher=teacher)


@app.route('/teachers/edit/<teacher_id>', methods=["POST"])
def process_edit_teacher(teacher_id):
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    db.teachers.update_one({
        "_id": ObjectId(teacher_id)
    }, {
        "$set": {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        }
    })
    return redirect(url_for('show_teachers'))


# DELETE STUDENT OR TEACHER PROFILE

@app.route('/students/delete/<student_id>')
def show_confirm_delete(student_id):
    students_to_be_deleted = db.students.find_one({
        "_id": ObjectId(student_id)
    })
    return render_template('students/show_confirm_delete.template.html',
                           student=students_to_be_deleted)


@app.route('/students/delete/<student_id>', methods=["POST"])
def confirm_delete(student_id):
    db.students.remove({
        "_id": ObjectId(student_id)
    })
    return redirect(url_for("show_students"))


@app.route('/teachers/delete/<teacher_id>')
def show_confirm_delete_teacher(teacher_id):
    teachers_to_be_deleted = db.teachers.find_one({
        "_id": ObjectId(teacher_id)
    })
    return render_template('teachers/confirm_delete_teacher.template.html',
                           teacher=teachers_to_be_deleted)


@app.route('/teachers/delete/<teacher_id>', methods=["POST"])
def confirm_delete_teacher(teacher_id):
    db.teachers.remove({
        "_id": ObjectId(teacher_id)
    })
    return redirect(url_for("show_teachers"))


# SEARCH

@app.route('/students/search')
def show_search_form():
    return render_template('search.template.html')


@app.route('/students/search', methods=['POST'])
def process_search_form():
    first_name = request.form.get('first_name')
    class_groupId = request.form.get('class_groupId')

    critera = {}

    if first_name:
        critera['first_name'] = {
            '$regex': first_name,
            '$options': 'i'  # i means 'case-insensitive'
        }

    if class_groupId:
        critera['class_groupId'] = {
            '$regex': class_groupId,
            '$options': 'i'  # i means 'case-insensitive'
        }

    searched_by = [first_name, class_groupId]

    results = db.students.find(critera)
    return render_template('students/display_student.template.html',
                           all_students=results,
                           searched_by=searched_by)


@app.route('/logout')
def logout():
    return redirect(url_for("home"))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
