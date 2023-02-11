# dorm-service-tracker
Tracks service hours and opportunities for dorm scholars of Ateneo de Manila University

## Command Cheatsheet
### If setting up the project for the first time on your local machine
1. Create a virtual environment (open cmd in dorm-service-tracker and do `python3 -m venv venv`)
2. Activate virtual environment (`venv\Scripts\activate`)
3. Install packages into your virtual environment (`pip install -r requirements.txt`)
4. Place `.env` file in your `dorm-service-tracker` folder

### If working on the project
- Activate virtual environment (`venv\Scripts\activate`)
- Run server (` python manage.py runserver`)
- IMPORTANT: Migrate your changes (`python manage.py migrate`)

## URLs
- Django Admin: http://127.0.0.1:8000/admin/