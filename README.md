📝 #Sticky Notes Application

The Sticky Notes application is a task management tool designed to help users efficiently organize and manage their tasks. It is built primarily using Python, with front-end components in HTML and CSS.

Features

🗂️ Task Management:

📋 Create, read, update, and delete tasks.
🗓️ Organize tasks with various attributes like due dates, priorities, and categories.
💻 User Interface:

🌐 A web-based interface built with HTML and CSS for easy task management.
🖱️ Interactive and user-friendly design to enhance user experience.
🗃️ Database:

💾 Uses SQLite3 for storing task data.
🔒 Ensures data persistence and reliability.
Project Structure

📈 CRUD Matrix.drawio: Diagram representing the Create, Read, Update, Delete operations for the application.
📋 Task manager app sequence Diagram.drawio: Sequence diagram illustrating the workflow of the task management application.
🗃️ db.sqlite3: SQLite3 database file storing all task-related data.
🚀 manage.py: The main script to run the Django application.
🗂️ notes/: Directory containing the core functionality for managing sticky notes.
📄 __init__.py: Initializes the notes module.
⚙️ admin.py: Configuration for the Django admin interface.
⚙️ apps.py: Application configuration for the notes app.
📝 forms.py: Contains forms for creating and updating notes.
📄 models.py: Defines the data models for the notes.
🔗 urls.py: URL declarations for the notes app.
👨‍💻 views.py: Contains the view logic for handling requests.
🧪 test.py: Contains test cases for the application.
🧪 tests.py: Contains additional test cases for the application.
🗂️ __pycache__/: Directory containing cached bytecode files.
🗂️ migrations/: Directory for database migration files.
🗂️ static/: Directory for static files specific to the notes app.
🗂️ templates/: Directory for HTML templates specific to the notes app.
🌐 static/: Directory for static files like CSS and JavaScript.
📦 sticky_notes/: Main application directory containing the core logic and configurations.
📄 __init__.py: Initializes the sticky_notes module.
⚙️ asgi.py: ASGI configuration for asynchronous web server interface.
⚙️ settings.py: Contains settings and configuration for the Django project.
🔗 urls.py: URL declarations for the Django project.
⚙️ wsgi.py: WSGI configuration for the web server gateway interface.
🗂️ __pycache__/: Directory containing cached bytecode files.
📋 task manager application use case Diagram.drawio: Use case diagram showing various use cases for the task management application.
📋 task manager class Diagram.drawio: Class diagram depicting the structure of the application classes.
Usage

⚙️ Setup:

🧩 Clone the repository.
📦 Install required dependencies.
🚀 Run the Django application using manage.py.
💡 Running the Application:

🌐 Navigate to the application URL in your web browser.
📋 Use the interface to manage your tasks effectively.
This repository provides a comprehensive framework for a task management application with detailed diagrams illustrating the system's design and functionality.

Note: For a complete view of the contents of the notes directory, please visit the sticky_notes/notes directory on GitHub. The contents listed include core modules and configurations essential for managing notes within the application.
