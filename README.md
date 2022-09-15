# COMP0035 Coursework 1 and 2 repository

# Coursework 1

## Technical information
### Repository URL

[Repository](https://github.com/ucl-comp0035/coursework-1-m0a5y7.git)

### Set-up instructions

Assume that requirements will be installed from requirements.txt.

If you have used any libraries that require set-up beyond `pip install ...` then use this section to explain any set-up
instructions to be followed to run your coursework.

If the marker cannot execute your coursework they can't grade it!


## Selection of project methodology
### Methodology (or combination) selected
CRISP-DM
### Selection criteria and justification of selection
According to [Data Science Process Alliance (n.a.)](https://www.datascience-pm.com/crisp-dm-2/), CRISP-DM is the most common methodology for data mining, analytics, and data science projects. It is a data-oriented process method, meaning that the main phases center around preparing, exploring and understanding the data.

Selection criteria: 
- Our understanding of the requirements of the project (if we do not, a flexible process method is more suitable):
  - The project requires us to prepare and analyse a dataset, with a clear end goal (quantifiable summary of green space in London boroughs). Being data-oriented and analytic is one of the strenghts of CRISP-DM.
- Expected lifetime of the project:
  - The product is used for deciding fund allocation now, but it should be kept live for the general public and any independent city planners to view, so maintenance should be arranged for at least the next ~3 years. With CRISP-DM, there is a lot of freedom in moving back and forth between phases, so it is possible to go back to previous steps if there is an update in the data.
- Risk (Do we know the domain very well? Do we know the technologies involved? If so, we might go with a more traditional process. If not, an agile and flexible one is better):
  - I have experience with this very same dataset from another module, and the rest of the team has experience building web applications. There are no anticipated risks with the project. CRISP-DM is a more traditional process, and thus suitable.
- Schedule constraints:
  - The Mayor would like to see the web application as soon as possible, within the next two months. CRISP-DM allows our team to efficiently focus on the most important aspect of the project: understanding the data. This will help us deliver the project within this tight schedule.


## Definition of the business need
### Problem definition
Source: [Mayor of London (n.a.)](https://www.london.gov.uk/about-us/mayor-london/mayor-and-his-team/role-mayor-london)

The Mayor of London has heard complaints from multiple boroughs that they are lacking green space and would like more funding in order to develop usable green spaces. However, the yearly funding reserved for environmental projects is not enough to cover all the boroughs that have raised complaints. The Mayor would like to accurately determine where green spaces are needed most and thus where to allocate funding, and has commissioned a team of developers to create a visual representation of how green space is divided in London, as well as any other analytics they can derive from the data available. If possible, The Mayor would like to prioritise boroughs that have already indicated non-green open space that could be converted, because it will be less costly and time-consuming than adding green space into pre-existing infrastructure.

### Target audience
The Mayor of London's assistant, who will present the results at a budget meeting, and city planners who want to use the data to justify their project proposals.

Persona 1 (Mayor's Assistant): <img width="1159" alt="Screenshot 2021-11-10 at 10 15 02" src="https://user-images.githubusercontent.com/92042636/141095322-be9d62f8-89e2-4f49-8d49-73a1d2fcc371.png">

Persona 2 (Independent city planner):<img width="1163" alt="Screenshot 2021-11-10 at 10 16 06" src="https://user-images.githubusercontent.com/92042636/141095440-7ef39395-0642-4f97-af1d-53b4572de2a9.png">



### Questions to be answered using the dataset
- Which boroughs in London have the least green space?
- Which parts of those boroughs need green space the most?
- Do the spaces with trees correspond to the open spaces?
- What are the open spaces that are not green? 
- Can they be used for further green development?
- Are there any potential geographical reasons for this uneven spread of green space (that might prevent green development)?

The web application will answer these questions by having a mapping function that combines the tree map and open space map. The information is split by borough, so a user can use the drop-down list functionality to check which borough has the most and which has the least green space/open space. Clicking on a borough will open information on it, such as names and locations of open spaces. Each open space will list how many trees are within it.

## Data preparation and exploration

### Data preparation

I had a lot of problems with downloading the london_street_trees_gla_20180214.csv dataset, the file was too big for my computer/internet connection to handle.
My original solution was to manually copy and paste it into Excel, but this messed up the formatting of the coordinate columns. I spent a lot of time trying to clean it up, but someone else was able to download the dataset for me. I am afraid I did not get as far with this project as I could have without this time-consuming issue.

[Data Preparation](data_preparation.py)

### Prepared data set

[Original data set (Trees)](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/790adc4e563301de599809dded1f60709b264e01/london_street_trees_gla_20180214.csv)
[Prepared data set (Trees)](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/790adc4e563301de599809dded1f60709b264e01/London_trees_cleaned.csv)

[Original data set (Open space)](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/790adc4e563301de599809dded1f60709b264e01/GiGL_openspace_subset_(beta)_V6.csv)
[Prepared data set (Open space)](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/790adc4e563301de599809dded1f60709b264e01/Openspace_cleaned.csv)

### Data exploration
As stated in Data Preparation, due to time constraints I was unable to complete all the steps I wanted for this coursework. Namely, I would have wanted to define a function named compare_trees_to_open, which finds the 5 boroughs with the least trees, then finds the unique types of open space in the same boroughs, and joins these two results into one dataframe. You can see my attempt to do this without a function in the data exploration code.

[Data Exploration](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/a150a17d2ab52f1027a6553ade31c22c005da185/data_exploration.py)
![Trees_by_borough_Histogram](https://user-images.githubusercontent.com/92042636/141143199-0cf64a5d-f79b-47d9-b6a1-e64ed2f6f648.png)
![Open_Space_by_Borough_Histogram](https://user-images.githubusercontent.com/92042636/141143225-49e9ba78-100b-47c4-ba97-ca0c5e23cca9.png)

## Weekly progress reports

### Report 1
What I did in the last week:
- Read through the coursework 1 specification. 
- Set up a GitHub account and completed PBL 1 problems
- I am also still deciding between two process methods, and will ask about it in today's tutorial.

What I plan to do in the next week:
- Finalise my process method
- Write a problem statement
- Start preparing the data

Issues blocking my progress (state ‘None’ if there are no issues):
- PyCharm did not recognise Python on my computer, so I was unable to set up a virtual environment when going through PBL 1 exercises. I will try again or ask advice during office hour.

### Report 2
What I did in the last week:
- Chose a process method (Kanban)
- Wrote a problem statement
- Wrote a persona
- Realised after writing those that Kanban is not the best method for my project and went back to choose another one

What I plan to do in the next week:
- (Before next week) I will finalise my process method choice, I think I will go for CRISP-DM because I need something traditional and data-oriented
- Prepare the data
- Explore the data

Issues blocking my progress (state ‘None’ if there are no issues):
- None
### Report 3
What I did in the last week:
- Made a list of data preparation steps I want to take for the CW dataset based on the problem class session

What I plan to do in the next week:
- Finish preparing the data and explore it
- Go back to previous week's tasks to ensure I have completed them satisfactorily

Issues blocking my progress (state ‘None’ if there are no issues):
- My computer had a lot of performance issues, which affected my ability to submit the status report on time and to fully finish the data preparation steps. But it seems to be working normally again.
### Report 4
What I did in the last week:
- Downloaded and cleaned my dataset (this was time-consuming, as it wouldn't download directly from the website and I had to copy and paste it into an Excel file. This however messed up the latitude coordinate data, which I needed for my original project idea.)

- Explored some different visualisations I could get out of the dataset.

What I plan to do in the next week:
- Finish it by checking all the steps are appropriately completed and then submit.

Issues blocking my progress (state ‘None’ if there are no issues):
- Because some of the data is formatted wrong, I either need to find a way to reformat it in the data preparation code, or rethink my project aim. This is stressful because the deadline is so close and both solutions might take a lot of valuable time from finishing the project.



## References

Data Science Process Alliance. 2021. CRISP-DM - Data Science Process Alliance. [online] Available at: <https://www.datascience-pm.com/crisp-dm-2/> [Accessed 10 November 2021].

The Mayor of London. 2021. The role of the Mayor of London. [online] Available at: <https://www.london.gov.uk/about-us/mayor-london/mayor-and-his-team/role-mayor-london> [Accessed 10 November 2021].

# Coursework 2

## Requirements

### Context Diagram

I created a [Context Diagram](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/365bb76cc9aff952e4d68d1926ab3b9990195650/COMP0035ContextDiagram.jpg) to better understand the stakeholders and their interaction with the application, in preparation for requirements elicitation.

### Requirements technique

#### Tecnique justification

Note: My process methodology is CRISP-DM. Because it's so data-oriented, there is no one specific requirement elicitation that best fits it. In the 'Business understanding' phase [(Vorhies, 2016)](https://www.datasciencecentral.com/profiles/blogs/crisp-dm-a-standard-methodology-to-ensure-a-good-outcome), the focus is on understanding requirements from a business perspective, and then converting them into a data mining problem definition. There is very little focus on the stakeholders, or the 'users' of the end result. Because we however do have users that will view and utilise the results, we will choose a requirement elicitation technique that, despite no specific justification within CRISP-DM, will help us fully understand our stakeholders.

From [Tiwari and Singh (2017)](https://arxiv.org/pdf/1709.08481.pdf), using the attribute matrix to figure out best method with solid justification:

- **Project size: Small (Calculated w COCOMO model)** Interview, focus group, observation, prototyping, scenarios/story board, analysis of existing domain, laddering, repository grid, task analysis, introspection, concept/mind mapping, online conversation

- **Project complexity: Low to medium** Brainstorming, interview, workshops, survey, protocol analysis, scenarios/story board, models, analusis of existing domain, laddering, repository grid, JAD/RAD, introspection, class responsibility collaboration, domain analysis, online conversation, document analysis

- **Requirement volatility: Small** Brainstorming, focus group, workshops, observation, ethnography/social analysis,, questionnaires, repository grid, domain analysis

- **Degree of criticalness: Low to medium** Brainstorming, focus group, workshops, observation, survey, protocol analysis, questionnaires, analysis of existing domain, laddering, repository grid, introspection, domain analysis, concept/mind mapping, online conversation, document analysis

- **Time and cost constraint: Budget low to medium** Brainstorming, interview, focus group, workshops, observation, ethnography, survey, prototyping, protocol analysis, card sorting,  laddering, introspection

- **Existing domain: Existing (London datastore's own visualisation for tree canopy)** Interview, focus group, observation, ethnography/social analysis, protocol analysis, card sorting, scenarios/story boarding, models, questionnaires, analysis of existing domain, laddering, repository grid, introspection, domain analysis, document analysis

- **Stakeholders availability: Low heterogeneous (Stakeholders all want similar things from the application)** Workshops, observation, ethnography/social analysis, survey, questionnaires, analysis of existing domain

- **Project reachability: Generic (because members of the public need access to it too)** Workshops, Survey, Scenarios/story board, models, repository grid, JAD/RAD, task analysis, introspection, class responsibility collaboration, concept/mind mapping, online conversation

- **Domain knowledge: Medium** Brainstorming, interview, workshops, ethnography/social analysis, prototyping, protocol analysis, scenarios/story board, models, questionnaires, analysis of existing domain, laddering, repository grid, task analysis, introspection, class responsibility collaboration, concept/mind mapping, online conversation, document analysis

- **Project type: Embedded** Interview, focus group, scenarios/story board, models, questionnaires, JAD/RAD, task analysis, introspection, class responsibility collaboration, domain analysis, document analysis

    Note: This method for justifying a requirements elicitation technique is quite time-consuming, but using it avoids the use of an 'arbitrary' technique without        consideration for others, especially in a real-world project that could make use of all the techniques. It also gave me an opportunity to think deeper about the nature of this project.

Brainstorming (5), interview (6), focus group (6), workshops (7), observation (6), ethnography (5), survey (5), prototyping (3), protocol analysis (5), card sorting (2), scenarios/story board (6), models (5), questionnaires (6), analysis of existing domain (5), laddering (6), repository grid (7), JAD/RAD (3), task analysis (4), introspection (8), class responsibility collaboration (4), domain analysis (5), concept/mind mapping (4), online conversation (5), document analysis (5)

→ With 8 matches, introspection is the most compatible technique. However, 'introspection' just refers to the software engineering imagining requirements. This should only be the starting point of requirements elicitation. Workshops and repository grid (repertory grid) have 7 matches, but cannot be used due to the ethical constraints of this project that prevent the inclusion of participants. Same goes for interviews, focus groups, observation, questionnaires, laddering. So, with 6 matches, scenarios/**story boarding** is the strongest contender without having to use real participants. 

List of "introspected" requirements:
- Visualisation tool for trees per borough
- Mapping of exact location of trees using coordinate data
- Visualisation tool for open space per borough, overlapped with the green space
- An option to only view non-green or green open space
- Clicking on borough will open borough-specific information on green and open spaces, including names
- Blog feature for boroughs to share updates on their green development

### Story Mapping

[Comakers LLC (n.d.)](http://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) details the use of story map concepts (**aka story boarding**) for eliciting requirements. The benefit of this technique is that it is user-centric, but focuses on both depth and width (aka both specificity of a single task, and sufficient amount of tasks in application). This would be a good technique for my application, because I could use the pre-existing personas and think further about what their specific needs are.

Small criticism of story mapping: because my application does not have a wide range of functionalities, I have a need for thinking about each one deeply, but not so much for organising a large amount of different tasks. You will see that there are some tasks which end up being quite similar because of this.

What: Tree and open space visualisation and analysis application

Who: Mayor who wants to decide budget, boroughs who can commission developers, developers who want to justify their proposals, general public who may be concerned with the greenery of their living area

[Story Map](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/fd7d111b5e295986c560f482559f45a16ef21fbd/Story_mapping.pdf)

### Prioritisation

Story mapping inherently considers the priority of a specific item: the higher up a task is, the more important it is. Alternative tasks or additional tasks will be lower in the map. Similarly, the left-most item will be the first thing a user would want to do in the application.

## Design
### Wireframes

[Link to Wireframe directory](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/cca1758c5cb04abeb6450a9165e14af2d49e85fc/Wireframes)

### Application Architecture with UML Diagram

For both the UML Diagram and the ERD I used a lucidchart template (Lucidchart, n.d.). The reason I chose to create the architecture with a UML diagram is because from the teaching materials it appeared to be the clearest technique. Additionally, it is also possible to create UML diagrams from pre-existing code in PyCharm [(UML class diagrams | PyCharm, 2021)](https://www.jetbrains.com/help/pycharm/class-diagram.html#analyze_class). It seemed useful to learn this technique because I may choose to use it in future projects as described in the article.

[Link to UML Diagram](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/a94c1eab8ac998aeeb2455847f7241b68e527ca8/UML%20class%20diagram%20COMP0035.png)

**Routes and views:**
- *Route*,               *View, (Wireframe number)* 

- '/dashboard',           Dashboard and home page, (1)
- '/dashboard/graph',     Graph view on dashboard, (2)
- '/dashboard',           The route doesn't change when opening the Upload or Import element, (3)
- '/blog',                Blog tab, (4)
- '/user/blog',           I considered that a logged in user will have a different route than a guest user, (5)
- '/blog/article1',       Tab for specific article in blog, (6)
- '/login',               Route that precedes /user route, (7)
- '/user/user_profile',   A logged in user's profile page, (8)


### Database Design with Entity relationship diagram

My choice of ERD is similar than for the UML Diagram: from the teaching materials it appeared to be a widely used technique so I found it useful to learn it.
[Link to ERD](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/482f4b8f09b1b6cd4b050c15759640de6cf81a63/ERDCOMP0035.png)


## Testing 

- Wrote two tests for the class in user.py (I also moved user.py inside the tests folder because importing it from outside was too problematic, I know this is not advisable usually).
- Wrote a fixture in conftest.py for a user object.
- Learned about code coverage and tried it out with pytest-cov:
[SCREENSHOT](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/72ec6f8c5ec0ebffeacfc00e7791122c45ae09de/CODECOVERAGE.png). It says that in the user.py file 74% of the code is covered. I assume this is because it counts the class definitions into the lines of code that are covered. In reality, I am testing 2/4 functions in the class. I wonder whether in a bigger program this would be an issue - half of the class methods are disregarded in testing but 74% is considered 'good' coverage. 
- Set up a continuous integration workflow on github with code coverage. Reading the [lint with flake8 report](https://github.com/ucl-comp0035/coursework-1-m0a5y7/blob/998894318cf8df7437ec39ee7699bc8c095e731b/Screenshot%202021-12-22%20at%2015.57.30.png), there were some style issues, but when I went to check the code, they were issues I had already fixed in PyCharm. Also, it says I imported things that I did not use (pytest and conftest), however, when I removed them the tests do not run. In a large-scale project having a tool such as this is ideal, because it reduces the time needed to run tests, and automates it. This allows the team to place more focus on other phases and to regularly check any major issues in a reliable way.

## References

Comakers LLC, n.d. Story Map Concepts. [online] jeffpatton&associates. Available at: <http://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf> [Accessed 22 December 2021].

Lucidchart. n.d. Welcome to Lucid. [online] Available at: <https://lucid.app/> [Accessed 22 December 2021].

PyCharm. 2021. UML class diagrams | PyCharm. [online] Available at: <https://www.jetbrains.com/help/pycharm/class-diagram.html> [Accessed 22 December 2021].

Tiwari, S. and Singh, S., 2017. A Methodology for the Selection of Requirement Elicitation Techniques. [online] Available at: <https://arxiv.org/pdf/1709.08481.pdf> [Accessed 22 December 2021].

Vorhies, W., 2016. CRISP-DM – a Standard Methodology to Ensure a Good Outcome. [online] Datasciencecentral.com. Available at: <https://www.datasciencecentral.com/profiles/blogs/crisp-dm-a-standard-methodology-to-ensure-a-good-outcome> [Accessed 22 December 2021].


