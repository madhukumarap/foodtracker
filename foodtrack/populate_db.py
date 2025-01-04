from foodtrack import create_app
from foodtrack.extension import db
from foodtrack.models import Food, Log

app = create_app()

with app.app_context():
    # Create some Food entries
    apple = Food(name="Apple", proteins=0, carbs=25, fats=0)
    banana = Food(name="Banana", proteins=1, carbs=27, fats=0)

    # Create a Log entry with the food
    log_entry = Log(date='2025-01-04', foods=[apple, banana])

    db.session.add_all([apple, banana, log_entry])
    db.session.commit()
    print("Data inserted successfully.")
