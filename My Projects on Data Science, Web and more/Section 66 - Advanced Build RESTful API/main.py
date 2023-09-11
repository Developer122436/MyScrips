from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)
EXPECTED_API_KEY = "TopSecretAPIKey"

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.before_request
def setup_db():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def get_random_cafe():
    cafe_ids = [cafe.id for cafe in Cafe.query.with_entities(Cafe.id).all()]

    if not cafe_ids:
        return jsonify(error="No cafes found"), 404

    randId = random.choice(cafe_ids)
    cafe = Cafe.query.get(randId)
    return jsonify(cafe=cafe.to_dict())


@app.route('/all', methods=['GET'])
def get_all_cafes():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route('/search/<string:loc>', methods=['GET'])
def get_cafe_on_location(loc):
    cafes = Cafe.query.filter_by(location=loc).all()

    if not cafes:
        return jsonify(error="No cafes found"), 404

    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )

    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    except Exception as e:
        db.session.rollback()
        return jsonify(response={"error": f"An error occurred: {e}"}), 500


## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    new_price = request.form.get("coffee_price")

    if not new_price:
        return jsonify(response={"error": "No new price provided."}), 400

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": f"Successfully updated the price for cafe with ID {cafe_id}."})


## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")

    if not api_key or api_key != EXPECTED_API_KEY:
        return jsonify(error="Invalid or missing API key."), 403

    cafe = Cafe.query.get_or_404(cafe_id)

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": f"Cafe with ID {cafe_id} has been deleted."})


if __name__ == '__main__':
    app.run(debug=True)
