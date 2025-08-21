# How to run

1. Create & activate a virtual environment
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (optional)
   ```bash
   python manage.py createsuperuser
   ```

5. Start the server
   ```bash
   python manage.py runserver
   ```

6. Open in browser
   - Home: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/adminpanel/dashboard/
