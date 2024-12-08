# ShareNote Backend

## Introduction
ShareNote is a platform designed to help students share and discover study notes. The backend is built with Django and Django REST Framework, providing a robust API that supports note sharing, user management, and content organization features.

## Features
- User authentication and profile management
- Note upload and management system
- Hierarchical content organization (Faculty → Degree → Course → Notes)
- Tagging system for enhanced content discovery
- File storage for notes and profile pictures
- RESTful API endpoints for all CRUD operations

## Technology Stack
- Python 3.x
- Django
- Django REST Framework
- SQLite (Development)
- CORS Headers

## Project Structure
share-note_backend/
├── backend_server/          # Main project directory
│   ├── backend_server/     # Project configuration
│   │   ├── init.py
│   │   ├── asgi.py        # ASGI configuration
│   │   ├── settings.py    # Project settings
│   │   ├── urls.py        # Main URL configuration
│   │   └── wsgi.py        # WSGI configuration
│   ├── notes_app/         # Main application
│   │   ├── migrations/    # Database migrations
│   │   ├── init.py
│   │   ├── admin.py      # Admin interface configuration
│   │   ├── apps.py       # App configuration
│   │   ├── models.py     # Database models
│   │   ├── serializers.py # API serializers
│   │   ├── tests.py      # Unit tests
│   │   ├── urls.py       # App URL patterns
│   │   └── views.py      # API views
│   ├── media/            # User-uploaded files
│   ├── db.sqlite3        # Development database
│   └── manage.py         # Django management script
└── env/                  # Virtual environment (not tracked in git)

## Installation and Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)
- virtualenv (recommended)

### Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd share-note_backend
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Navigate to the project directory:
```bash
cd backend_server
```

5. Set up the database:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

The API will be available at http://localhost:8000/

## API Endpoints

### User Management
- `GET/POST /user/` - List users or create new user
- `GET/PUT/DELETE /user/<id>` - Retrieve, update or delete user

### Profile Management
- `GET/POST /profile/` - List profiles or create new profile
- `GET/PUT/DELETE /profile/<id>` - Retrieve, update or delete profile

### Notes
- `GET/POST /note/` - List notes or create new note
- `GET/PUT/DELETE /note/<id>` - Retrieve, update or delete note

### Subjects and Tags
- `GET/POST /subject/` - List subjects or create new subject
- `GET/PUT/DELETE /subject/<id>` - Retrieve, update or delete subject
- `GET/POST /tag/` - List tags or create new tag
- `GET/PUT/DELETE /tag/<id>` - Retrieve, update or delete tag

### File Management
- `POST /save_file` - Upload files

## Models

### User Profile
- Extends Django's built-in User model
- Additional fields for bio and profile picture

### Note
- Title, content, and optional file attachment
- Created and updated timestamps
- Owner relationship to User model

### Subject and Tag
- Name field with unique constraint
- Used for note categorization

### Relationships
- NoteTag: Many-to-many relationship between Notes and Tags
- NoteSubject: Many-to-many relationship between Notes and Subjects

## Development Guidelines

### Database Migrations
When making model changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests
```bash
python manage.py test
```

## Contributing

Fork the repository
Create a feature branch
Make your changes
Run tests
Submit a pull request
