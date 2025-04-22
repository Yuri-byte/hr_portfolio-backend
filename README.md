
---

## ✅ `README.md` for the **backend (Django API)**

```markdown
# HR Org Chart – Backend API

This is the **Django backend** for the HR Org Chart application. It provides a REST API to serve hierarchical employee data to a frontend built in React.

### 🔗 Live API

👉 [https://hr-portfolio-luil.onrender.com/api/employees/](https://hr-portfolio-luil.onrender.com/api/employees/)

---

## 🚀 Features

- Django + Django REST Framework
- Hierarchical employee relationships (manager → reports)
- Tree-style JSON endpoint for frontend consumption
- Individual employee profile endpoint
- CORS-enabled for frontend integration
- Ready for Render deployment

---

## 🧱 Tech Stack

- Django
- Django REST Framework
- SQLite (or PostgreSQL)
- Gunicorn
- Render (for deployment)

---

## 🔧 Setup & Run Locally

```bash
git clone https://github.com/Yuri-byte/hr_portfolio-backend
cd hr_portfolio-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py loaddata fixtures/roles_fixture.json
python manage.py loaddata fixtures/employees_fixture.json
