from .extension import db
log_food = db.Table('log_food',
    db.Column('log_id', db.Integer, db.ForeignKey('log.id') , primary_key=True),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_key=True)
)
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)
    #@property is a decorator that allows you to define methods that behave like attributes.
    @property
    def calories(self):
        return self.proteins*4 + self.carbs*4 + self.fats*9
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    foods = db.relationship('Food', secondary=log_food, backref='log_dates')
