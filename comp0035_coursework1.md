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


