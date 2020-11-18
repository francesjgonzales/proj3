# Student Attendace Tracker 

A website that help teachers manage student attendance record.

You may access the deployed website [here] (https://fg-proj3-student-attendance.herokuapp.com/). 

 
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
The **colour palette** used are [loud colours](readme/colourPalette.png) to suit kids' preference. (*after usability testing, main purple color was toned down and instead use an orange color to compliment the main color. Also, the final project shows 2 main colors. The secondary colors will be used in further development)
The **images** used are cartoon-like especially the student profiles where kids can choose what type of image they can use for their profiles.
The **font** used is a [Red hat](https://fonts.google.com/specimen/Red+Hat+Text#license) font style. I picked this one because of its playful look and easy readability for teachers and kids.


### Wireframes

Desktop wireframes found [here](https://www.figma.com/proto/cnpk9XUHqG4NUYYtuwLCJz/proj3-sat?node-id=25%3A55&viewport=-46%2C1453%2C0.3348211646080017&scaling=contain) is created to perform in the teacher user's view, student's and parent's view. It may be different from the deployed as during the usability testing along the way for easier access and navigation.

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

A search bar with a dropdown button that shows **Students** & **Class group** info as hints to user on what categories they can search. This was the initial plan but during the usability testing, I decided to move this to be in the center page so that teachers can easily refer to and categories were separated for easier access. This is helpful when shown in mobile 

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

### Parents tasks
Parents have the similar sign up and login method as the teacher. At this stage, they can view their kids profiles. In later development, they can get access to attendance and communicate with teachers on their school updates and social development

### Search bar
It has 3 search categories, Student's name, Class Group and Teachers name. When the submit button is clicked with blank inputs, it will lead to display page showing the Student's Main Database. If they key in under either of the 3 categories, it will still lead to the display page showing the Student's Main Database. 

For later stage of development, I will sort the display page according to the categories and the Principal or School Manager will only have the private access to the Student Main Database. 

### Mobile Responsive
This website is mobile responsive and can be used in mobile and tablets. 


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
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)
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
