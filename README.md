# Nota 

**Nota** is a Django-based blog application built as a side-project to sharpen my Django and Software Engineering skills.

---

## Table of Contents
- [⚙️ Local Setup](#-local-setup)
- [✨ Features](#-features)
- [🪪 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## ⚙️ Local Setup

To run Nota in development mode, make sure that the `DEBUG` setting in `config/settings/base.py` is set to `True`.

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/nota.git
    cd nota
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file using the following template:
    ```env
    DEBUG_SECRET_KEY=your-secret-key
    DEBUG_ALLOWED_HOSTS=localhost,127.0.0.1
    ```

5. Apply migrations and run the development server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## ✨ Features

- [ ] Create posts
- [ ] Markdown support
- [ ] Comment on posts
- [ ] Read-Later list
- [ ] Admin interface
- [ ] Post tagging
- [ ] User authentication

*_(Features are a work in progress and subject to change.)_*

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---
