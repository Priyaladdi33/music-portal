# Music Portal 🎵

## Description
The Music Portal is a feature-rich web application developed using Django. It allows users to explore, filter, and play music by various genres, complete with album artwork and artist information. The platform supports responsive design and ensures a smooth user experience across devices.

## Features
- **User Authentication**: Register, login, and manage accounts securely.
- **Audio Playback**: Stream songs directly from the browser.
- **Filter by Tags**: View songs categorized by tags like Hindi, Kannada, and English.
- **Responsive UI**: Fully responsive design with Bootstrap integration.
- **Dynamic Media**: Upload and display song files and images dynamically.

---

## Prerequisites

- Python 3.x
- Django 4.x
- Database: SQLite (default) or any other Django-supported database.
- Media file support for images and audio.

---

## Setup Instructions

### Clone the Repository
bash
git clone https://github.com/Priyaladdi33/music-portal.git
cd music-portal

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd music-portal
   

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**
   Run the following command to apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

7. **Configure Media and Static Files**
   - Add media files (images and songs) to the appropriate directories.
   - Ensure `MEDIA_URL` and `MEDIA_ROOT` are correctly configured in `settings.py`.

## Project Structure
```
MusicPortal/
├── accounts/            # App for user authentication
├── musicApp/            # Main app for managing songs
│   ├── migrations/      # Database migrations
│   ├── templates/       # HTML templates
│   ├── static/          # Static files (CSS, JS, images)
│   └── models.py        # Song model definition
├── media/               # Media files (uploaded images and songs)
├── requirements.txt     # Project dependencies
├── manage.py            # Django management script
└── README.md            # Project documentation
```

## Usage
1. Log in or create an account.
2. Browse the list of all songs on the homepage.
3. Use the navigation to filter songs by tags (Hindi, Kannada, English).
4. Play songs directly from the browser.

## Example Song Model
```python
from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    song_file = models.FileField(upload_to='songs/')
    tags = models.CharField(max_length=50)  # E.g., 'Hindi', 'Kannada', 'English'

    def __str__(self):
        return self.name
```

## Technologies Used
- Django (Backend framework)
- SQLite (Default database; configurable to other databases)
- HTML, CSS, and Bootstrap (Frontend)

## Media and Static File Configuration
Ensure these settings in `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

## License
This project is licensed under the MIT License. Feel free to use and modify it.

## Acknowledgments
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/

---
Happy Coding!

