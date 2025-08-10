### Learning Tracker

A console-based Python application for tracking and managing learning activities. This tool provides a simple yet robust way for a single user to log study sessions, view history, and gain insights into their learning habits. All user data is securely stored locally in a JSON file.

### Features

-   **User Authentication**: Secure registration and login.
-   **Activity Logging**: Record learning topics, time spent, and notes.
-   **Data Persistence**: All data is automatically saved to and loaded from a JSON file.
-   **Activity Management**: View and filter learning sessions by topic or date.
-   **Statistics**: Get insights on total time, number of activities, and average time per session.

### Getting Started

1.  **Prerequisites**: Python 3.x is required.
2.  **Setup**: The code uses a hardcoded file path (`D:\Python\JSONS\users.json`). **You must update this path** to your desired file location.
3.  **Execution**: Run the main script from your terminal: `python learning_tracker.py`

### Future Scope

This project serves as a solid foundation for more complex applications. Potential upgrades include transitioning to a web application using Django, implementing a RESTful API, and adding advanced features like data visualization and password hashing.