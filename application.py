from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        return f'{self.name} - {self.description}'

@app.route('/')
def index():
    return "Hello  wrld!"

@app.route('/drink')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = { 'name': drink.name, 'description': drink.description}
        output.append(drink_data)

    return {"drinks": output}