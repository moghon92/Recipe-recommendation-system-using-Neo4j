# [REMARK]
This is a windows Application

# [DESCRIPTION] 

## 1. Application description
- Welcome to Our novel recipe recommendation App. Our app uses collaborative and content-based filtering for recommendation rather than just text-based search. In addition, our interactive UI allows the users to select the most relevant ingredients based on its relevance to the main ingredient as well as suggesting alternate ingredients.

- Neo4j, a graph database, is chosen as the database management tool for our implementation. The DB has a three-layer graph with User to User, Recipe to Recipe, Ingredient to ingredient and Recipe to Ingredient relationships between all three types of nodes.

- The UI for our recipe recommender is user-based, in which different users can login to their account and search for recipes. As soon as the user login, they will reach the main page of the recommender. It shows the short cuts to the user’s record, as well as the input fields for the main ingredient and side ingredients. User can decide to have the search result in graph/table presentation by selecting “Visual/Text” search option.

## 2. Package description
This software package is structured as follows:-
	- DOC folder which contains the project report and poster
	- CODE folder which contains our aplication and database. The code folder contains:
		-- [DB] folder which contains our (neo4j) DB
		-- [RecEngineScripts] folder which contains the (python) scripts used for generating recipe, user & ingredients simmilarties
		-- [RecApp] folder which contains the code for the front end (flask, d3, HTML/CSS).

# [INSTALLATION]

## Prerequisite Software
Make sure your enviroment is setup up properly with the below software:-

1. windows 10
2. Java (JDK 11.0)
3. Python 3.7 or higher
4. Add the path to your python and pip under the PATH variable in your enviroment variables
	- follow the instruction in the below links for more guidance on how setup your envirment variables on windows
	https://datatofish.com/add-python-to-windows-path/
	
**To test your setup open your command line/terminal and run :
	- java --version      ----------> openjdk 11.0.x
	- python --version    ----------> Python 3.7+
	- pip --version       ----------> pip 21.0+

** No Further installation is required

# [EXECUTION]
A. To start up the Application follow the 2 steps below:
	1. download the DB from this link
https://gtvault-my.sharepoint.com/:u:/g/personal/preddemreddy3_gatech_edu/Eb2zq6EUAlBBgLQ8T_3F_4oBEVqGZ13SBhuUZv3NbrQo1A?e=CwcYRI
	2. unzip and save the folder named "DB" under the CODE folder of the submissison
	3. run "neo4j_start.bat" to spinup the graph database 
	4. run "app_start.bat" to start the web App

[optional]
B. In case you face any errors running the 2 scripts above, you can follow the step by step process outlined below:
	1. Open a new cmd window
	2. Make sure you are in the CODE folder
	3. Start neo4j 
		- run DB\bin\neo4j console
	4. Open a new cmd window
	5. Go to the RecipeApp folder 
		- cd RecipeApp 
	6. Install python virtual enviroment
		- pip install virtualenv
	7. Activate the virtual enviroment
		- venv\Scripts\activate
		- in case above command fails run "source venv/bin/activate" instead
	8. Install the required packages in the virtual environment
		- pip install -r requirements.txt
	9. start the App
		- python app.py
	10. Start chrome and open the frontend
		- start chrome http://localhost:5020/
		
# [DEMO VIDEO]
- How to startup the App
	https://youtu.be/gVwVud7gsHQ
- RecApp demo
	https://www.youtube.com/watch?v=M4le6ZxOFCQ

***For more info visit out github repo:
https://github.gatech.edu/hyan88/Europe-Team-Project
