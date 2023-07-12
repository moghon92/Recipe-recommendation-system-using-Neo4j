cd RecipeApp
pip install virtualenv==20.4.4
virtualenv -p python3.7 venv
cd venv\Scripts & activate & cd ../../ & pip install -r requirements.txt & start chrome http://localhost:5020/ & python app.py