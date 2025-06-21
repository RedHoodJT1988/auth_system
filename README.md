# 🛡️ Django Authentication System
A fully functional user authentication system built with Django 5 that covers all the essentials:
- ✅ User Registration
- ✅ Login & Logout
- ✅ Profile Update
- ✅ Password Change & Reset
- ✅ CSRF protection and secure session handling

This project is perfect as a starter for more complex applications that require user management.

---

## 🚀 Features
- **User Signup**: Create an account with email and password.
- **User Login & Logout**: Secure login and logout flow using Django's built-in auth.
- **Profile Page**: View and update user profile details like name and email.
- **Password Change**: Users can change their current password while logged in.
- **Password Reset via Email**: Users can request a password reset link if they forget their password.
- **Mobile-Responsive Templates**: Uses Bootstrap and NES.css (customizable to your needs).
- **Clean & Extendable Code**: Easily hook in new fields, signals or views.

---
## 🛠️ Tech Stack
- **Backend**: Django 5.x
- **Frontend**: Django Templates + Boostrap + NES.css
- **Email Backend**: Console backend for dev(`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend')
---

## 📦 Installation
1. **Clone the Repo**:
```bash
git clone https://github.com/yourusername/django-auth-system.git
cd django-auth-system
```
2. **Create and Activate Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
4. **Apply Migrations**:
```bash
python manage.py migrate
```
5. **Create a Superuser (optional)**:
```bash
python manage.py createsuperuser
```
6. **Run the Development Server**:
```bash
python manage.py runserver
```
7. Visit: http://127.0.0.1:8000/ in your browser and explore!

---
## 🧪 Development Setup
Ensure you have the following apps in `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',          # <-- Your custom app
    'widget_tweaks',     # Optional for template forms
]
```

---

## 📨 Email Configuration (For Password Reset)
During development, console email backend is used.
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
To use a real email provider (like Gmail or SendGrid), update your settings:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

---

## 📁 Project Structure
```bash
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── registration/  # login.html, signup.html, password_reset.html, etc.
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── auth_system/
│   ├── settings.py
│   ├── urls.py
├── templates/
│   └── base.html
├── manage.py
```
---

## ✅ Routes Overview
| URL                          | Description                 |
| ---------------------------- | --------------------------- |
| `/accounts/signup/`          | User registration           |
| `/accounts/login/`           | Login                       |
| `/accounts/logout/`          | Logout                      |
| `/accounts/profile/<pk>/`    | Profile page                |
| `/accounts/password_change/` | Change password             |
| `/accounts/password_reset/`  | Reset password (send email) |

---

## 👨‍💻 Author
Developed by [Jonathan Reeves](https://github.com/RedHoodJT1988)
Built during a #30DaysOfPython challenge and refined with love (and many restarts).