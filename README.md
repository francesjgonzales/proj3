# Student Attendace Tracker 

A website that help teachers manage student attendance record.

You may access the deployed website [here] (http). 

 
## UX

This website is designed for teachers to register the student, assign them to a class group, track each student's attendance and temperature, and update student records. Teachers will be the main user in this website and in later development, parents will be the secondary user where communication and chat group will be created. This website is for internal use where parents will be given special access by teachers. 


### User Story

This idea came about when the student care where my son goes to implemented a safe entry procedure in light of the pandemic that the government imposed for all Student Cares. The teacher takes their temparature and writes it down on their file record. When the student leaves the place, they have access to this file record to write the time they logout. 

I want to propose a digital version so that teacher can easily record the student's temperature and clock in time. 


### User Profiles

#### Teachers
- Aged 20-40 years old
- Digitally competent
- Always multi-tasking


#### Parents
- Middle-age group
- Digitally competent
- Prefers paperless transactions


#### Students
- Aged 6-11 years old
- has basic knowledge of how to use iPad and Mobile 


### Design

The layout design is inspired by the app called [Class Dojo](https://www.classdojo.com/en-gb/?redirect=true) where I referred to how students and classes are organised.
The **colour palette** used are [loud colours](readme/colourPalette.png) to suit kids' preference. 
The **images** used are cartoon-like especially the student profiles where kids can choose what type of image they can use for their profiles.
The **font** used is a [Red hat](https://fonts.google.com/specimen/Red+Hat+Text#license) font style. I picked this one because of easy readability for teachers and kids.


### Wireframes

Desktop wireframes found [here](https://www.figma.com/proto/cnpk9XUHqG4NUYYtuwLCJz/proj3-sat?node-id=25%3A55&viewport=-46%2C1453%2C0.3348211646080017&scaling=contain) is created to perform in the teacher user's view, student's and parent's view.

The link also served as an interactive prototype to test if the database relationship is working.


## Features

### Existing Features
The website will feature the following

#### Introduction page

A one-liner description of the website and the name is shown and accompanied by **Sign up** and **Login** buttons. 

When either buttons clicked, it will go to the next page to determine who is accessing the page, a teacher or a parent. 


#### Sign up / Login page

When the user clicked on the desired role, the user will go to this page where:
In **sign up**, they need to key in their names, email and password. 

In **login**, they need to key in their email and password. 


#### Teacher's main page

In this page, the user will see the students' list assigned to a specific group. The user can add, edit, update and delete a student profile.


#### Parent's main page

In this page, the user will see their child's profile which includes, their names and date of birth and which class group they are assigned to. 


#### Student's main page

In this page, the teacher is the only one who can access this page. The user will see the name of the student, date of birth and status of their attendance which is labelled as either 'present' or 'absent'. This list is editable and can be deleted. The user can also add a student's profile here. 


#### Attendance page

In this page, the teacher is the only one who can access this page. The user can log in the timings of when students comes in and out of the student care. The user can also add in the temparature of each students. If there's a change in the details, the user can click on edit button to update the information. 


#### Search bar

A search bar with a dropdown button that shows **Students** & **Class group** info as hints to user on what categories they can search. 

Here are additional features to be implemented in the future:

### Features Left to Implement
- Expand the student profile by adding skills and social development
- The student profile expansion is used by teachers to update the parents on their children. 
- An internal chatroom between teacher and parents for one-on-one communication

## Technologies Used

- Figma for wireframing and design
- Illustrator for vector images to convert to svg
- Python
- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files)
- HTML
- CSS
- JavaScript
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for cloud hosted database



## Programming Methodologies
Requirements when working with the following:

- Work with python
``` 
pip3 install flask
```

- Work with user authentication
```
pip3 install flask-login
```

```
pip3 install dnspython
```

- Generate Python key. Paste the secret key into the separate py file called 'generate-key.py' file
```
python3 generate-key.py
```

- Access MongoDB database
```
pip3 install pymongo
```

- Allows me to install variables. This will not be pushed to GitHub because of confidential info.
```
pip3 install python-dotenv
``` 


- .env file was used to store environment variables so that Flask secret key and database credentials were not publicly viewable.

## Database Design

Here's the [ER] diagram of this project's data base. 

Three MongoDB collections were used:


### Sample MongoDB documents
Here are sample database documents for each user

#Teacher (represents one teacher)
```
{
   “_id”: ObjectId(“123445”);
   “first_name: “Agnes”,
   “last_name: “Rosario”,
   “email”: “teacheragnes@sat.com”,
   “password: “password1234”,
 }
```

#Teacher’s list 
```
{
  “teacher_id”: ObjectId(“123445”);
  “class_groupID”: ObjectId(“1111”),
}
```

#Class Group
```
{
  “_id”: ObjectId(“123”);
  “student_id”: (“222”),
  “clock_in”: 1:00pm,
  “calendar”: 06Nov2020,
}
```

#Student (represents one student)
```
{
   “_id”: ObjectId(“333”);
   “first_name”: “Bennett”,
   “last_name”: “Snerf”,
   “date_of_birth”: 04112010,
}
```

#Attendance
```
{
  “student_id”: “333”;
  “clock_in”: 1:00pm,
  “clock_out”: 6:00pm,
  “temperature”: 36.5,
  “calendar”: 23Nov2020,
  “class_groupID”: “123”,
  “remarks”: On medical leave
}
```

#Parent  (represents one parent)
```
{
   “_id”: ObjectId(“444”);
   “first_name: “Bert”,
   “last_name: “Snerf”,
   “email”: “mrsnerf@gmail.com”,
   “password: “password1234”,
}
```

#Family
```
{
  “student_id”: “333”;
  “parent_id”: “444”;
}
```


## Testing

### To check whether the MongoDB is working in Flask I typed this code and check terminal for MONGO_URL to appear 
```
print(os.environ.get('MONGO_URL'))
```

### When CSS didn't respond after refreshing the page, type
```
command + shift + readability
```

I created 2 user logins for this page, **Teacher** and **Parent**. At this stage of the project, my focus is to get the flow of the website and improve on ux. Authentication will be done on second part of the project.

### Both users have similar forms to fill up on login and sign up.

Here are given tasks performed by **Teacher** in order to achieve certain goals.

1. Sign up an account (This is similar to parent's sign up too)

   1. CREATE teacher's account to get access to class groups, student list and attendance.
    - Form includes First and last names of the user, email and password.  
   2. After signing up, teacher will be lead to **Teacher's profile page**, 
   
2. Add a student, access attendance and delete student profile

    Once the teacher get an access, a brief explanation of what this page is about and clickable buttons are shown:

    - **Attendance**, to view the student's profile and attendance. 

        - **Add Student** The teacher adds student profile by filling up form that includes the first and last names, date of birth, Class group and teacher assigned to class group. 

        - **Clock in and clock out** The teacher can input the time on when the student enters and leaves the student care. (*During usability testing, the user thought that she also has to key in the timing during the registration process since these were part of the form.) 

        - **Temparature check** teacher can key in the student's temparature for COVID-19 contract tracing purpose.

        - **Edit** teacher can edit the student profile by editing the registration form, clock in and out and temparatures. 

        - **Delete** Teacher can delete the student's profile which includes, first and last names, date of birth, clock in and out, temparature, class group and teacher.

    - **Search**, to search based on Student name, Class Group and Teacher's name. 

        - **Display Search** The user will see the results based on what they searched about.


Here are given tasks performed by **Parent** in order to achieve certain goals.

1. As explained above, sign up is similar to teacher. 

### 


This website is mobile responsive and can be used in mobile and tablets. 


## Deployment


This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
- The bootstrap validation form code was copied from [https://mdbootstrap.com/docs/jquery/forms/validation/]
- Showing current time code was copied from [https://stackoverflow.com/questions/28415178/how-do-you-show-the-current-time-on-a-web-page]
- Parsing and Formatting Dates in Python with datetime by Pretty Printed [https://www.youtube.com/watch?v=zY02utxcauo]

### Media
- The parents icon used in the website is made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
- The teacher icon used in the website is made by <a href="https://www.flaticon.com/authors/monkik" title="monkik">monkik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
- The student icons used in the website are credited as follows:
    - Raphael icon is made by <a href="" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    - Puffer fish icon is made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    
- Vector image used in main page is made by <a href="https://www.freepik.com/vectors/people">People vector created by benzoix - www.freepik.com</a>
- Calendar icon is made by Icons made by <a href="https://www.flaticon.com/authors/bqlqn" title="bqlqn">bqlqn</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

### Acknowledgements

- I received inspiration for this project from X
