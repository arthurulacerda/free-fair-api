from flask import Flask
from flask_restful import Api

from config import mysqlConfig
from resources.v1.fair import Fair, FairList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'Dese.Decent.Pups.BOOYO0OST'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Fair, '/v1/fair/<int:fair_id>')
api.add_resource(FairList, '/v1/fair')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
