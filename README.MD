# 🎬 IMDB Clone REST API (Django + DRF)

A backend REST API project built using Django and Django REST Framework for managing movies, streaming platforms, and user reviews.
This project demonstrates real-world backend development including CI/CD, Docker, and deployment.

---

## 🌐 Live Demo

🔗 **[Click here to open the application](https://imdb-clone-drf.onrender.com/)**

👉 Visit the homepage to explore all available API endpoints.

---

## 🚀 Features

* RESTful APIs for movies, streaming platforms, and reviews
* User authentication (Login, Register, Logout)
* CI/CD pipeline using GitHub Actions
* Docker containerization
* Deployment on Render using Gunicorn
* Simple homepage for navigating API endpoints

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite / PostgreSQL
* **Version Control:** Git, GitHub
* **CI/CD:** GitHub Actions
* **Containerization:** Docker
* **Deployment:** Render, Gunicorn

---

## 📌 API Endpoints

### 🎥 Watchlist

* `/list/` → List all movies
* `/list2/` → Alternate list view
* `/<id>/` → Movie detail

### 📺 Streaming Platforms

* `/stream/` → List platforms
* `/stream/<id>/` → Platform detail

### ⭐ Reviews

* `/<id>/review-create/` → Create review
* `/<id>/reviews/` → List reviews
* `/review/<id>/` → Review detail
* `/reviews/` → User reviews

### 🔐 Authentication

* `/login/` → Login
* `/register/` → Register
* `/logout/` → Logout

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/manjunadh967/imdb-clone-drf.git

# Navigate into project
cd imdb-clone-drf

# Create virtual environment
python -m venv myvenv

# Activate environment
# Windows
myvenv\Scripts\activate
# Mac/Linux
source myvenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## 🐳 Docker Setup

```bash
# Build Docker image
docker build -t imdb-django .

# Run container
docker run -p 8000:8000 imdb-django
```

---

## 🤖 CI/CD Pipeline

This project uses GitHub Actions to:

* Install dependencies
* Run Django checks
* Execute tests
* Perform linting using Flake8

---

## 👨‍💻 Author

**Manjunadh Gobburu**
🔗 https://github.com/manjunadh967
