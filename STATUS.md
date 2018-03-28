# Quantifying Corruption Status Report
**Team number:** 9  

**Team members:**
- Andrey Karnauch  
- William Lifferth  
- Kelsey Veca  
- Chris Dean  

## Introduction
Since our proposal, we have made a fair amount of progress on our project. The project currently consists of a **splash** page with a search bar and a minimalistic **search** page. Furthermore, the functionality behind conducting a search has been put in place as well, meaning a database is queried and responses are shown. In terms of deployment, the project has successfully been deployed on Heroku, viewable [here](http://quantifying-corruption.herokuapp.com/).

In terms of changes and major events since our proposal:
 - Deciding to Dockerize our project
 - Increasing dependency on our customer to deliver their data
 - Using D3.js for data visualization

## Customer Value
Changes in Customer Value/Requirements/Measures of Success:
1. No data being received on Bills
   - **Date**: Sprint 3
   - **Motivation**: Time constraints
   - **Desc**: We were orginally going to be receiving donation data both on legislators and bills, however, we are now only receiving data on legislators, which is still fine and narrows our scope.
2. Honing on NRA donations
   - **Date**: Sprint 3
   - **Motivation**: Current events
   - **Desc**: Our customer is now also honing in on NRA donations that legislators receive due to the changing political climate.
3. "Provide a search bar that queries the customer's database"
   - No changes, still a main requirement that is on track
4. "Display results of searches in an elegant and meaningful manner"
   - **Date**: Sprint 4
   - **Motivation**: Desire to meet the "elegant and meaningful" Requirements
   - **Desc**: This Measure of Success was built on during Sprint 4 when we decided to use D3.js for visualization. We believe this will help us both meet the original requirement and also extend it to something more meaningful.
5. "Deliver a modern looking set of pages and styling to attract users"
   - **Date**: Sprint 3
   - **Motivation**: Thematic elements to go along with "political corruption"
   - **Desc**: Rather than just going for a purely modern look, we decided to adjust this requirement a bit to also account for thematic elements. We ended up with a combination between modern and symbolic for our splash page.

## Technology

**Architecture**:

The core framework we're using for this project is Django which is written in Python. Django by default uses a SQLite database to store default django records (mostly users) and our custom models. We utilize the Jinja templating engine to put custom data into our html web pages, and a bootstrap frontend with vanilla javascript. We are hosting our project on a Heroku backend that supplies us with a platform without needing to configure or maintain our own virtual server; the Heroku backend uses a PostgreSQL database.

**Goals**:
- Our most recent goal was to have a sense of functionality within our website. We had the splash page set up and a legislator model in Django, but lacked any functionality between the static page and our database. Thus, our goal was to implement the search functionality required to query the database and then display the gathered information.

**What Works**:
  1. Successful deployment on Heroku: View [here](http://quantifying-corruption.herokuapp.com/)
  2. Splash/search page: ![View](https://i.imgur.com/AHjr1dy.jpg)
  4. Search functionality: ![View](https://i.imgur.com/BfFvzvw.jpg)

**Tests Run**:
  - Accessing the web-app from several devices.
  - Navigation bar redirection
  - Search button functionality
  - Returned search data vs. data in the database

**Upcoming Goals**:

For our next iteration, we are planning to focus heavily on the data/customer aspect of this project. We are hoping to obtain a lot more data, transfer this data from local to online storage, and work on visualization of returned search data. We feel this is an integral part of our project which needs to be addressed over the next couple of weeks in order to having a "working" product.

## Team
Team member roles since the start of this project:
  1. William Lifferth
     - Project lead, main contributor and project designer
  2. Andrey Karnauch
     - Initial html/styling and organizing issues/sprints
  3. Chris Dean
     - Initial Heroku integrator and model designer
  4. Kelsey Veca
     - UX Engineer

Going forward, these roles are expected to change a bit. William will continue to take on his leading role with the rest of team trying to provide more support throughout these last couple of sprints. For example, Andrey will be dealing with D3 visualization, Chris will be working with Docker, and Kelsey will be working on the **About** page along with updating the navbar.

## Project Management
As of now, the product is on schedule, but we would have liked to maybe be just a bit further down the road. However, with that being said, we are happy with our current site and are eager to add more functionality as the customer delivers more data.

Since the start of the semester, the schedule has changed quite a bit. For example, we struggled with dragging certain elements of the project out over sprints and instead ended up doing them within short bursts instead. Also, we have not communicated with our customer as often as we would have liked, which means we have to establish a strong line between our team and theirs within these last couple of sprints in order to meet requirements and deliver a "working" product.

## Reflection
- What went well?
  - For the most part, we organized our Github issues and milestones pretty well. In terms of our product, we came together on a symbolic yet modern looking theme for the website.  We also felt good about the demo recently and our ability to transition into providing functionality within our product.
- What did not go well?
  - One of our weakest points since the start has been poor communication with our customer, which has to change here soon. Also, we did not all carry our weight equally during this iteration, which is something we have addressed as a team recently by assigning new, meaningful issues/tasks for everyone.
- Next iteration?
  - In this next iteration, we are looking to improve on both our communication with our customer and our own teamwork. We hope to stay on track for Sprint 4 and meet our goals as a team, which will require both data from our customer and each team member working on their assigned issue.
