# Student Attendace Tracker 
<img src="static/images/website_mockup.jpg" style="margin:0">

A website that help teachers manage student attendance record.

You may access the deployed website [here] (https://fg-proj3-student-attendance.herokuapp.com/). 

**Teacher and Parent sign up and login**, this project don't require user authentication, there's no login details provided. Tester have to key in at least 1 character for all input fields to be able to access it.
 
## UX

This website is designed for teachers to register their student, assign them to a class group, track each student's attendance & temperature, and update student's profile. For the purpose of this submission, teachers are able to access the main student database where they can perform tasks like register, edit student profile, update attendance and delete student profile. 

In later development, there will be princicap user which is the manager of student care to access the main student database and control which teachers can perform CRUD tasks. Also parents will be the secondary user where communication and chat group will be created. This website is for internal use where parents will be given special access by teachers. 


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
The **colour palette** used are [loud colours](readme/colourPalette.png) to suit kids' preference. (*after usability testing, main purple color was toned down and instead use an orange color to compliment the main color. Also, the final project shows 2 main colors. The secondary colors will be used in further development)
The **images** used are cartoon-like especially the student profiles where kids can choose what type of image they can use for their profiles.
The **font** used is a [Red hat](https://fonts.google.com/specimen/Red+Hat+Text#license) font style. I picked this one because of its playful look and easy readability for teachers and kids.


### Wireframes

Desktop wireframes found [here](https://www.figma.com/proto/cnpk9XUHqG4NUYYtuwLCJz/proj3-sat?node-id=25%3A55&viewport=-46%2C1453%2C0.3348211646080017&scaling=contain) is created to perform in the teacher user's view, student's and parent's view. It may be different from the deployed as during the usability testing along the way for easier access and navigation.

The link also served as an interactive prototype to test if the database relationship is working.


## Features and User Stories

### Existing Features
The website will feature the following:

#### Home page

A one-liner description of the website and the name is shown and accompanied by **Sign up** and **Login** buttons. 

When either buttons clicked, it will go to the next page to determine who is accessing the page, a teacher or a parent. 

#### Sign up / Login page

When the user clicked on the desired role, the user will go to these pages based on their roles (To implement user authenticaton in later development):
In **sign up**, they need to key in their names, email and password. 

In **login**, they need to key in their email and password. 

#### Teacher's main page

In this page, the user will see the students' list assigned to a specific group. The user can add, edit, update and delete a student profile and attendance. 


#### Parent's main page

In this page, the user will see their child's profile which includes, their names and date of birth and which class group they are assigned to. 


#### Student Attendance page

In this page, the teacher is the only one who can access this page. The user can log in the timings of when students comes in and out of the student care. The user can also add in the temparature of each students. If there's a change in the details, the user can click on edit button to update the information. 


#### Student Profile page

In this page, the user can edit or delete a student's first and last names, date of birth, assigned class group and teacher. 

#### Search page

A search page with a dropdown button that shows **Students** & **Class group** info as hints to user on what categories they can search. This was the initial plan but during the usability testing, I decided to move this to be in the center page so that teachers can easily refer to and categories were separated for easier access. This is helpful when shown in mobile.

#### Mobile Responsiveness

The website can be viewed on mobile and tablet. The tables in student attendance are also responsive with the ability to swipe to right to view the rest of columns. 


| User Stories   |      Features      |  Remarks |
|----------|:-------------:|------:|
| Teacher is able to click on the link to SAT app |  Homepage | Pass |
| Teacher is able to click on **Teacher Sign up** to create an account |    Teacher sign up page   | Pass |
| Teacher is able to click on **Teacher Login** to login with no authentication required | Teacher login | Pass |
| Teacher is able to access on **Teacher Main** after logging in or signing up | Teacher Main Page | Pass |
| Teacher is able to click on **Student Attendance** and update timings in student's attendance | Student Attendance Page | Pass |
| Teacher is able to edit or delete students' first and last names, class group, temperature and remarks  | Student Attendance Page | Pass |
| Teacher is able to edit or delete a student's first & last names, date of birth, class group and assigned teacher | Student Profile Page | Pass |
| Teacher is able to click on **Search page** to search by student's name, class group or teacher  |  Search Page | Pass |
| Parent is able to click on the link to SAT app |  Homepage | Pass |
| Parent is able to click on **Parent Sign up** to create an account |    Parent sign up page   | Pass |
| Parent is able to click on **Parent Login** to login with no authentication required | Parent login | Pass |
| Parent is able to access on **Parent Main** after logging in or signing up | Parent Main Page | Pass |
| Teacher and Parent to be able to check from the mobile and tablet | Mobile responsiveness | Pass |


**Here are additional features to be implemented in the future:**

### Features Left to Implement

#### Students skills page
The teacher can use this page to add, edit and update a student's academic and social development skills. This will help them update the parents. **Part of Teacher & Student pages enhancement**

#### Internal Chatroom page
An internal chatroom between teacher and parents for a two-way communication about a student's academic and social skills.  This will also help teachers disseminate announcements or news about student care. **Part of Teacher page enhancement**

#### User Authentication
Teachers and parents user authentication will be implemented. This will verify the identity of users who have signed up and authorise them to access the website. 

#### Parents and Teachers' profiles
To implement a CRUD on parent and teacher profiles.

#### Parent page enhancement
To add more features like **status of student's attendance** and **internal chatroom** with teachers.

#### Mobile Responsiveness
To improve the tables and display the whole content that fits depending on the device.

| User Stories   |      Features      |  Remarks |
|----------|:-------------:|------:|
| Teacher to edit or delete his/her profile |  Teacher Profile page | To be implemented |
| Teacher to log in student's academic and social skills | Student's skills page | To be implemented |
| Teacher to send out announcement about student care's important dates to parents | Internal Chatroom | To be implemented | 
| Teacher to send and reply on parent's messages | Internal Chatroom | To be implemented |
| Teacher to verify account upon sign up via email sent or OTP sent | User Authentication | To be implemented |
| Parent to edit or delete his/her profile | Parent Profile | To be implemented |
| Parent to check on child's attendance status on what time they clocked in and clocked out from student care | Parent page | To be implemented |
| Parent to send a message to teacher about child's attendance | Internal Chatroom | To be implemented | 
| Parent to view student's academic and social skills sent by Teacher | Student's skills page | To be implemented |
| Parent and teacher to view student's attendance, student profiles or search results in 1 page without swiping or scrolling | Mobile responsiveness | To be implemented |


## Technologies Used

- Figma for wireframing and design
- Illustrator for vector images to convert to svg
- Python
- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files)
- HTML
- CSS
- JavaScript
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for cloud hosted database
- [https://validator.w3.org/]


## Programming Methodologies
Requirements when working with the following:

- Work with python
``` 
pip3 install flask
```

- Work with user authentication. (*This will be develop in the later stage of the project)
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

**ER** diagram of this project's data base can be access [here]((readme/diagram-SAT.pdf))

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
   "teacher_list": [
       {
           “teacher_id”: ObjectId(“123445”),
           "class_groupId": ObjectId(“123”),
           "student_id": ObjectId(“333”);
           "attendance_id": ObjectId("2345345")
       }
   ]
 }
```

#Student (represents one student with embedded documents to access to attendance id) 
```
{
   “_id”: ObjectId(“333”);
   “first_name”: “Bennett”,
   “last_name”: “Snerf”,
   “date_of_birth”: 04112010,
   "attendance": [
       {
        "attendance_id": ObjectId("2345345");
        “clock_in”: 1:00pm,
        “clock_out”: 6:00pm,
        “temperature”: 39,
        “calendar”: 23Nov2020,
        "remarks": on medical leave
       },
       {
        "attendance_id": ObjectId("5354563");
        “clock_in”: 1:30pm,
        “clock_out”: 7:00pm,
        “temperature”: 36.5,
        “calendar”: 23Nov2020,
        "remarks": present
       },    
   ]
}
```

#Parent (represents one parent with embedded document to access to one student profile and attendance)
```
{
    “_id”: ObjectId(“444”);
    “first_name: “Bert”,
    “last_name: “Snerf”,
    “email”: “mrsnerf@gmail.com”,
    “password: “password1234”,
    "family": [
        “student_id”: “333”;
        "attendance_id": ObjectId("2345345);
    ]
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


#### USER TESTING
Please refer to **Features and User Stories**.


## Deployment
I created a git repository from github. Here are the steps on how to create

**Create Repository**
1. Login to [github](https://github.com/)
2. In main page, click on **New** button found in upper left corner. 
3. In repository name, type your project name. 
4. Select as public
5. In *initialise this repository with*, select **Add a README file**
6. Click on **Create Repository**
7. In the created repository, click on **Add file** to upload local files. 
8. Inside the created repository, I clicked on **Gitpod** where I'm directed to the gitpod page. I worked the entire project in here. 


**Gitpod workspace**
1. Go to source control, click the plus sign and type your meaningful commit message and click the tick sign to commit. 
3. Go to terminal and type `git push`
4. Go to [github](https://github.com/) account to check.


**Deploying in Heroku**
I followed the steps given by our instructor, Paul. 
1. Create a requirements.txt file and save in main folder.
2. Sign up for Heroku account [here](www.heroku.com)
3. Login to Heroku via gitpod main terminal. (*Once you have the access, key in the same account name and password used when signing up for Heroku account.*) 
4. Create a new app (*where the app-name will be replaced with your own created app.py file*)
5. Add new remotes 
6. Install gunicorn
    - "Procfile" is created and saved in same file as where the app.py file is. 
    - Inside the file, add in the app filename ensure that text is only 1 line. 
7. Install requirements file using **pip3 freeze --local > requirements.txt**
8. Set python flask debug to False
9. Commit everything using the following:
```
git add .
git commit -m "<Commit Message>"
```
10. Push to Heroku
```
git push heroku master
```
11. Go to Heroku

**Heroku**
1. Go to your assigned app file
2. In settings, go to Config Vars to add in the Mongo_URL and Secret_key.

My deployed project can be accessed [here](https://fg-proj3-student-attendance.herokuapp.com/)


## Credits

### Content
- The bootstrap validation form code was copied from [https://mdbootstrap.com/docs/jquery/forms/validation/]
- Showing current time code was copied from [https://stackoverflow.com/questions/28415178/how-do-you-show-the-current-time-on-a-web-page]
- Parsing and Formatting Dates in Python with datetime by Pretty Printed [https://www.youtube.com/watch?v=zY02utxcauo]
- Children's image take from [freepik](https://www.freepik.com/free-photo/funny-boy-genius-wearing-glasses-studio-shot_4745414.htm#page=1&query=asian%20child&position=41)
- Attendance image photo by Jeswin Thomas on Unsplash
- Search image photo by Glenn Carstens-Peters on Unsplash
- Student profile image photo by NeONBRAND on Unsplash

### Media
- The parents icon used in the website is made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
- The teacher icon used in the website is made by <a href="https://www.flaticon.com/authors/monkik" title="monkik">monkik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
- The student icons used in the website are credited as follows:
    - Raphael icon is made by <a href="" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    - Puffer fish icon is made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    
- Vector image used in main page is made by <a href="https://www.freepik.com/vectors/people">People vector created by benzoix - www.freepik.com</a>
- Calendar icon is made by Icons made by <a href="https://www.flaticon.com/authors/bqlqn" title="bqlqn">bqlqn</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

### Acknowledgements

- I received inspiration for this project from my son's student care. 
