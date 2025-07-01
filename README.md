# 📝 Personal Notes Manager

A simple Django-based web app for managing personal notes.  
Features include user authentication and CRUD operations for notes.

---

## 🚀 Features

- User Signup/Login using Django Auth
- Create, View, Update, Delete Notes
- User-specific note storage
- Responsive UI using Bootstrap
- SQLite database for easy setup

---

## 🔧 Tech Stack

- Django
- Django REST Framework
- SQLite
- Bootstrap (for styling)

---

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/personal-notes-manager.git
cd personal-notes-manager
```

2. **Create virtual environment and activate it**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Create a superuser**
```bash
python manage.py createsuperuser
```
6. **Run the development server**
```bash
python manage.py runserver
```
7. **Access the app**
   Admin Panel: http://127.0.0.1:8000/admin/
   Notes UI: http://127.0.0.1:8000/notes-ui/

---
## ⚠️ Note

This project does not include MySQL credentials.
If using MySQL or any other DB, please update settings.py accordingly.

---
