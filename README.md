# Django Backend for React + Vite Frontend

This folder (`main/backend/`) contains the Django backend for the React + Vite frontend.

## ✅ Completed Setup

### 📁 Folder Structure
- Frontend: `main/frontend/`
- Backend: `main/backend/`

### ⚙️ Project Setup
- Initialized Django project (`config`)
- Created virtual environment
- Installed necessary packages:
  - `django`
  - `djangorestframework`
  - `django-cors-headers`
  - `djangorestframework-simplejwt` (for JWT-based auth)

### 🔒 Authentication
- Implemented JWT-based login using cookies
- On successful login:
  - `access` and `refresh` tokens are stored in **HTTP-only cookies**
- Example API endpoint created:
  - `POST /api/login/` – authenticates user and sets cookies

### 🔄 CORS Configuration
- Enabled CORS to allow frontend access:
  - `http://localhost:5173` (Vite dev server)
- Allowed credentials to support cookie-based auth

### 🧱 Models
- Created custom user model (based on `AbstractUser`) in `core/models.py`
  - Ready to extend for future fields

---

## 🚀 How to Run

1. Navigate to `main/backend/`
2. Create virtual environment and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
