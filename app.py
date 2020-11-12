from flask import Flask, render_template, request, redirect, url_for, flash
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import pymongo


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


# TEACHER SIGN UP
@app.route('/teachers/create')
def show_create_teacher():
    return render_template('create_teacher.template.html')


@app.route('/teachers/create', methods=["POST"])
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
    return redirect(url_for('show_teachers'))


# TEACHER LOGIN

@app.route('/teachers/login')
def teacher_login():
    return render_template('login_teacher.template.html')


@app.route('/teachers/login', methods=["POST", "GET"])
def process_teacher_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if len(email) == 0:
        flash("Name cannot be empty", "error")
        return redirect(url_for('teacher_login'))

    db.teachers.find_one({
        'email': email,
        'password': password
    })
    return redirect(url_for("show_teachers"))


# PARENT SIGN UP

@app.route('/parents/create')
def show_create_parent():
    return render_template('create_parent.template.html')


# HOME

@app.route('/')
def home():
    return render_template('home.template.html')


# READ

@app.route('/students')
def show_students():
    all_students = db.students.find()
    return render_template('all_students.template.html',
                           all_students=all_students)


# TEACHERS LIST

@app.route('/teachers')
def show_teachers():
    all_teachers = db.teachers.find()
    return render_template('all_teachers.template.html',
                           all_teachers=all_teachers)


# TEACHER MAIN PAGE

@app.route('/teachers/main')
def show_teacher_main():
    return render_template('teacher_main.template.html')


# PARENTS MAIN PAGE

@app.route('/parents')
def show_parents():
    all_parents = db.parents.find()
    return render_template('all_parents.template.html',
                           all_parents=all_parents)


# CREATE STUDENT PROFILE

@app.route('/students/create')
def show_create_student():
    return render_template('create_student.template.html')


@app.route('/students/create', methods=["POST"])
def process_create_student():
    first_name = request.form.get("sfirst_name")
    last_name = request.form.get("slast_name")
    date_of_birth = request.form.get("sdate_of_birth")

    new_record = {
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth
    }

    db.students.insert_one(new_record)
    return redirect(url_for('show_students'))


# UPDATE STUDENT AND TEACHER PROFILE

@app.route('/students/edit/<student_id>')
def show_edit_student(student_id):
    student = db.students.find_one({
        '_id': ObjectId(student_id)
    })
    return render_template('edit_student.template.html', student=student)


@app.route('/students/edit/<student_id>', methods=["POST"])
def process_edit_student(student_id):
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    date_of_birth = int(request.form.get("date_of_birth"))

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
    return render_template('edit_teacher.template.html', teacher=teacher)


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
    return render_template('show_confirm_delete.template.html',
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
    return render_template('show_confirm_delete_teacher.template.html',
                           teacher=teachers_to_be_deleted)


@app.route('/teachers/delete/<teacher_id>', methods=["POST"])
def confirm_delete_teacher(teacher_id):
    db.teachers.remove({
        "_id": ObjectId(teacher_id)
    })
    return redirect(url_for("show_teachers"))


@app.route('/logout')
def logout():
    flask_login.logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('login'))
    

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
