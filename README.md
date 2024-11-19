# Final340
Creating a Database with a python frontend that will help students in ISAT find the course that they need to graduate.


File structure:
ISAT_Course_Finder/
│
├── app/
│   ├── __init__.py            # Makes `app` a Python package
│   ├── main.py                # Entry point for running the application
│   ├── controllers/           # Contains controllers for handling routes
│   │   ├── __init__.py
│   │   ├── courses.py         # Handles endpoints related to courses
│   │   ├── requirements.py    # Handles endpoints related to major requirements
│   │   └── students.py        # Handles endpoints related to students
│   │
│   ├── models/                # Handles database interaction
│   │   ├── __init__.py
│   │   ├── database.py        # Database connection setup
│   │   ├── courses.py         # Logic for fetching and updating course data
│   │   ├── requirements.py    # Logic for fetching requirements
│   │   └── students.py        # Logic for fetching and updating student data
│   │
│   ├── templates/             # Jinja2 HTML templates for rendering pages
│   │   ├── base.html          # Base template (common layout)
│   │   ├── courses.html       # Course listing page
│   │   ├── requirements.html  # Major requirements page
│   │   └── plan.html          # Graduation plan page
│   │
│   ├── static/                # Static assets (CSS, JS, images)
│       ├── css/
│       │   └── styles.css     # Custom styles
│       ├── js/
│       │   └── scripts.js     # Custom JavaScript
│       └── images/
│           └── logo.png       # Application logo
│
├── config/
│   ├── config.py              # Configuration file for database and app settings
│   └── logging.conf           # Logging configuration
│
├── data/
│   └── initial_data.sql       # SQL file for setting up initial database data
│
├── tests/
│   ├── __init__.py
│   ├── test_courses.py        # Test cases for course functionality
│   ├── test_students.py       # Test cases for student functionality
│   └── test_requirements.py   # Test cases for requirement functionality
│
├── requirements.txt           # List of Python dependencies
├── run.py                     # Script to start the CherryPy server
├── README.md                  # Documentation for the project
└── .gitignore                 # Ignore unnecessary files in version control

