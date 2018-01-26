# Quantifying Corruption Project Proposal
William Lifferth
Chris Dean
Andrey Karnauch
Kelsey Veca

## Introduction
The United States spent 3.15 billion dollars on lobbying in 2016. The trend of lobbying in the United States
has only risen over the years. Lobbying is intended to give the stakeholders of certain policies a direct method
of communicating with their representatives. The failing of this system is that it gives disproportionate amount
of influence to those with more financial resources. This creates an undesirable scenario where those with more
economic resources will pursue goals that reinforce their control over those resources, without regard for the
well-being of others. Previously this issue has been explored statistically, but in order to truly be made operational it must be presented in an format that is both accessible and easily understood.

We plan to create a free web app to allow the average citizen to check how their representatives are behaving. The lack of clear monetization strategies has discouraged market forces from producing a similar offering, so ours will be the first of its kind.

## Customer Value
### Customer Need
Our customer consists of a group of students currently participating in an independent study. Their study dives deep into how lobbyist/donator party affiliation affects the political party affiliation of the representatives on the receiving end. This project requires lots of data analysis to track every donation made to every representative and has the potential to shed light on some representatives who are more "corrupt" than others based on how much donors' party affiliation sways theirs.

The customer wants our team to take these findings and present them in a web app that is accessible to anyone curious about certain government representatives and their level of "corruption" based on the criteria above. With our help, the customer's base project gains a new level of meaning by not only identifying potential patterns of corruption, but also informing the citizens of America about these findings (by making the database searchable).

Because this project has the potential to reveal a lot about politicians in a time when politics are an extremely hot topic, we could expect to receive some recognition in the context of the market, whether it is user traffic, offers from interested third parties, or more. However, this relies both on the customer's final product in conjunction with ours, and the exposure of our web app once finished.

### Proposed Solution
Our team's solution will deliver a web application that queries the customer's database of government representatives that have been analyzed. The customer will have control over what goes in the database, and our web app will simply help search it and help visualize/display the results for the users.

This benefits the customer by allowing them to focus solely on filtering through donation history and identifying correlations between lobbyists and representatives, hopefully resulting in more accurate results on their end. Furthermore, the customer can work with us directly to dictate any styling, form submission, or graphic decisions that they envision for their base project.

### Measures of Success
Because of our direct, in-person communication with the customer, we will know if our product is satisfactory or not based on constant communication. Furthermore, we can see as a group whether or not we have met their requirements along with the goals we set for ourselves at the start of the project. For example, did we deliver just a search bar that spits out raw database data for each name searched, or did we produce an elegant search interface with partial matching and formatted results? These customer-centric measures of success are as follows:
- Provide a search bar that queries the customer's database
- Display results of searches in an elegant and meaningful manner
- Deliver a modern looking set of pages and styling to attract users

## Technology
### Heroku
We'll use a heroku hobby dyno to host any apps or services we may make; this will allow us to not worry to much about our server environment while also keeping costs low.
### SQLite/Postgres
Per our use of heroku we'll use relational SQL databases to store all production data. This may be on a SQLite database during development, or a Heroku Postgres database in production.
### Python 3.X
We'll use python as our serverside language and we'll use the most current stable version of it, which at time of writing is python 3.6. Most versions of Python 3 should work, but 3.6 is the standard.
### Django
Django enforces good practices and it's "batteries included" approach will allow us work only on the parts of our app that are important and novel.
### Bootstrap
We'll use bootstrap 3 for basic styling upon which we'll put our own styling.
### Other stuff
We'll try to keep things simple and only use tools when they're needed. We'll use whitenoise for serving static files, javascript and jquery where necessary, and things like photoshop if the need arises. We will not use any front end frameworks, "compile to css" languages, or anything else that makes our tech stack more cluttered.

## Team
### Dean, Chris
Chris Dean is a is a student at the University of Tennessee studying computer science and mathematics. He is the Events Directory of HackUTK and Volunteer Coordinator of Volhacks Hackathon.
- Skills
  - Python
  - SQl
  - Javascript
- Roles
  - Heroku Integrator
  - Model Designer

### Karnauch, Andrey
Student at UT, majoring in Computer Science with a minor in cyber security.
- Skills
  - C/C++, Python, LaTeX
  - Little experience with web development
  - New to most of the tools used in this project
- Roles
  - Assigned: Templates and styling
  - Fixed role at the start, fill in as needed

### Lifferth, William
William Lifferth is a student at the University of Tennessee studying computer science and machine learning. He is the president of the VolHacks Hackathon and the UTK Machine Learning club.
- Skills
  - Python
  - Django
  - Node.js
  - Web Development
  - SQL
- Roles
  - Engineering Lead
  - Solutions Architect
  - Data Scientist

### Veca, Kelsey
Kelsey Veca is a student of the University of Tennessee - Knoxville studying computer science and Spanish. She is a volunteer coordinator of the VolHack Hackathon club.
- Skills
  - C / C++
  - HTML / CSS
  - JavaScript
- Roles
  - UX Engineer

## Project Management
### Constraints

Although we have considered the potential for emotional and professional ramifications, we feel the obligation expose political corruption. We also recognize that we cannot accept donations from political parties as that could influence our message and reliability.

### Resources

This is a joint project to collect and present corruption data. The information will be provided by another team.

### Descoping

If we are unable to implement all the desired functionality, our system will still be able to operate at some capacity. It will at the very least act as a reference for political corruption. It could, however, be missing some features that would improve utility and user-friendliness.

### Schedule
_This is a rough schedule that is subject to change_
- Sprint 1: Django project set up that deploys to heroku and serves a blank page
- Sprint 2: Static templates for all our views
- Sprint 3: Models and databases are built and integrated locally and on heroku
- Sprint 4: Views (generally called controllers outside of django) built to deliver data to served templates
- Sprint 5: Search functionality finished
- Spring 6: Data visualizations finished

## Reflection
Our team is proposing a website to display data about governmental corruption. For this project our customer is anyone interested in promoting a free and open government, such as govermnent monitoring firms or the general population. We are all very excited to put together this project
