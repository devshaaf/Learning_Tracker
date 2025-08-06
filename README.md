# Learning_Tracker
This is a console-based application designed to help users track and manage their learning activities. It provides functionalities for user authentication, logging daily study sessions, viewing activity history, filtering activities, and displaying overall learning statistics. All user and activity data is persistently stored in a local JSON file.

Features
User Authentication: Secure user registration and login with username and password.

Activity Logging: Record new learning sessions including the topic, time spent (in minutes), and additional notes.

Data Persistence: All user accounts and their associated activities are automatically loaded from and saved to a JSON file, ensuring data is preserved across sessions.

View Activities: Display a comprehensive list of all logged learning activities for the current user.

Filter Activities: Easily search and filter activities by specific topics or by date (using the YYYY-MM-DD format).

Learning Statistics: Get insights into your learning habits with calculated totals for time spent, number of activities, and average time per activity.

Robust Input Handling: Includes basic input validation to guide users and prevent common errors.

How to Run
Prerequisites:

Python 3.x installed on your system.

No external libraries are required; the project uses built-in Python modules (datetime, json, re).

File Setup:

Create a JSON file named users.json in a directory of your choice.

Important: The current code has a hardcoded file path: D:\Python\JSONS\users.json. You must change this path within the load_data() and save_data() functions to match the actual location of your users.json file on your system.

Execution:

Navigate to the directory containing the learning_tracker.py (or whatever you've named your main Python file) in your terminal or command prompt.

Run the script using:

python learning_tracker.py

The application will then present you with the main menu options.

Code Structure
The project is organized using Object-Oriented Programming (OOP) principles:

User Class:

Represents an individual user of the application.

Stores username, password, and a list of Activity objects specific to that user.

Includes a to_dict() method for easy conversion to a dictionary format, suitable for JSON serialization.

Activity Class:

Represents a single learning entry.

Stores topic, time (in minutes), note, and the date the activity was logged.

users Global List:

A list that holds all User objects loaded from the users.json file when the application starts.

load_data() Function:

Handles reading the users.json file.

Parses the JSON data and reconstructs User and Activity objects from the dictionaries, populating the users global list.

save_data() Function:

Converts all current User objects (and their nested Activity objects) into a list of dictionaries.

Writes this data back to the users.json file, ensuring all changes are saved.

register_User() Function:

Allows new users to create an account with a unique username and a password.

login_User() Function:

Handles user authentication, prompting for username and password.

Includes a limited number of login attempts before locking the session.

log_activity() Function:

Guides the user through inputting details for a new learning activity.

display_user_activities() Function:

Prints a formatted list of all activities for a given user.

filter_activities() Function:

Takes user input to filter activities by topic or date and then displays the results.

show_stats() Function:

Calculates and displays summary statistics for a user's learning activities.

user_menu() Function:

The main menu displayed after a user successfully logs in, providing options to manage activities.

main_menu() Function:

The entry point of the application, allowing users to register, log in, or exit.

Future Improvements
This project serves as a strong foundation and can be expanded in many exciting ways:

Web Application Development: Transition from a console-based application to a full-fledged web application using a framework like Django. This would involve:

Replacing console inputs/outputs with web forms and HTML templates.

Utilizing Django's ORM (Object-Relational Mapper) to manage data in a proper database (e.g., SQLite, PostgreSQL) instead of a JSON file.

RESTful API Integration: Implement a RESTful API using Django Rest Framework (DRF). This would allow:

Your web front-end (or any other client, like a mobile app) to interact with your data programmatically.

Integration with tools like Swagger/OpenAPI for automated API documentation and testing.

Advanced Features:

Implement features like editing and deleting individual activities.

Add more sophisticated reporting and visualization of learning data (e.g., charts for time spent per topic over time).

Implement password hashing for better security (instead of storing plain text passwords).

Allow users to update their profile information.

Improved Error Handling: More granular error handling and user feedback for various scenarios.
