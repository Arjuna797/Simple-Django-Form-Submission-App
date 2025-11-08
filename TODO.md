# TODO: Transform Django Project to Notes App

- [x] Create a new Django app called 'notes' using `python manage.py startapp notes`
- [x] Add 'notes' to INSTALLED_APPS in myproject/settings.py
- [x] Define Note model in notes/models.py (fields: title, content, created_at)
- [x] Update notes/views.py to handle listing notes and creating new notes
- [x] Create notes/urls.py with URLs for notes (list and create)
- [x] Update myproject/urls.py to include notes.urls
- [x] Update templates/index.html to display list of notes and a form to add new notes
- [x] Run `python manage.py makemigrations` and `python manage.py migrate` to set up the database
