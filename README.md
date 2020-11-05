# Student Attendace Tracker 

A website that help teachers manage student attendance record.

You may access the deployed website [here] (http). 

 
## UX
This website is designed for teachers to register the student, assign them to a class group, track each student's attendance and temperature, and update student records. The purpose of this website is for teacher to have access to the database where all records are inside. 


**User Story**
This idea came about when the student care where my son goes to implemented a safe entry procedure in light of the pandemic that the government imposed for all Student Cares. The teacher takes their temparature and writes it down on their file record. When the student leaves the place, they have access to this file record to write the time they logout. 

I want to improve this process to be digitised so that teacher can easily record the student's temperature and clock in time. 


**User Profiles**

#### Teachers
- Aged 20-40 years old
- Digitally competent
- Always multi-tasking


#### Parents
- Middle-age group
- Digitally competent
These are the tasks Teachers are expected to perform
    1. Create a parent account to get access to the website
    2. In the main page, they can view their child's profile and attendance record 
    3. In attendance, they are expected to see the child's time of clock in the school and temparature record. 


#### Students
- Aged 6-11 years old
- iPad and Mobile users


Desktop wireframes found [here](readme/wireframes.pdf) is created to perform in the teacher user's view, student's and parent's view.

Tasks performed by **Teacher** in order to achieve certain goals.
   1. CREATE teacher's account to get access to class groups, student list and attendance. 
   2. In the main page, they are expected to the following buttons: **MY CLASS GROUP**, **ADD CLASS GROUP**, & **Agenda**



  

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used
- Python
- HTML
- CSS
- JavaScript
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for cloud hosted database

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

## Programming Methodologies
- .env file was used to store environment variables so that Flask secret key and database credentials were not publicly viewable.

## Database Design
Here's the [ER] diagram of this project's data base. 

Three MongoDB collections were used:


### Sample MongoDB documents
Sample database document for user:
```
{
   “_id”: ObjectId(“121837”);
   "name": "Joe Bookreader",
   "attendance": [
                {
                  "Time in": "1pm",
                  "Time out": "6pm",
                  "Temperature": "MA",
                  "Date": "29-11-2020"
                  “Comment": "29-11-2020"
                },
              ]
 }
```
## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


}
```
#Vet document (represent 1 vet)
	“id”: ObjectId(“123”);
	“first_name”: “Sue;
	“last_name”: “Mart”;
	“address”: “1234 Telok Blangah”
	“licence”: “1234”
}

#Check up (this is a document reference - 1st method in showing relationship)
```


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The parents icon used in the website is made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
- The teacher icon used in the website is made by <a href="https://www.flaticon.com/authors/monkik" title="monkik">monkik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
- The student icons used in the website are credited as follows:
    - Raphael icon is made by <a href="" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    - Puffer fish icon is made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
- 

### Acknowledgements

- I received inspiration for this project from X
