# init_db.py
from foodtrack import create_app
from foodtrack.extension import db

app = create_app()
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
