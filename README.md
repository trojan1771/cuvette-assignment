1. Clone the Repository:
Clone your project repository to your local machine using a Git command:
git clone https://github.com/trojan1771/cuvette-assignment

2. Navigate to the Project Directory:
Change your current working directory to the project folder:

cd your_project_name

3. Set Up a Virtual Environment:
Create and activate a virtual environment to isolate your project dependencies:

python -m venv venv

On Windows, activate the virtual environment:

venv\Scripts\activate

On macOS or Linux, activate the virtual environment:

source venv/bin/activate

4. Apply Migrations:
Apply database migrations to create the necessary database tables:

python manage.py migrate

5. Run the Development Server:
Start the Django development server:

python manage.py runserver

Visit http://127.0.0.1:8000/user/register in your web browser to see your application

Register a new user by visiting http://127.0.0.1:8000/user/register/.
Log in with the registered user at http://127.0.0.1:8000/user/login/.
Explore the dashboard at http://127.0.0.1:8000/user/dashboard/ and the profile at http://127.0.0.1:8000/user/profile/.
Log out at http://127.0.0.1:8000/user/logout/

If you make changes to the models or other database-related aspects, remember to apply migrations (python manage.py makemigrations and python manage.py migrate).

