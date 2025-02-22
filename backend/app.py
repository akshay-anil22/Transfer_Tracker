from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:akshay%401324@localhost:3306/transfertracker"
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = "players"
    
    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    last_season = db.Column(db.Integer)
    current_club_id = db.Column(db.Integer)
    player_code = db.Column(db.String(100))
    country_of_birth = db.Column(db.String(50))

    country_of_citizenship = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    sub_position = db.Column(db.String(50))
    position = db.Column(db.String(50))
    foot = db.Column(db.String(10))
    height_in_cm = db.Column(db.Integer)
    contract_expiration_date = db.Column(db.Date, nullable=True)
    agent_name = db.Column(db.String(100))
    image_url = db.Column(db.String(255))
    url = db.Column(db.String(255))
    current_club_domestic_competition_id = db.Column(db.String(10))
    current_club_name = db.Column(db.String(100))
    market_value_in_eur = db.Column(db.Integer)
    highest_market_value_in_eur = db.Column(db.Integer)

@app.route("/players", methods=["GET"])
def get_players():
    players = Player.query.all()
    return jsonify([{
        "id": p.player_id,
        "first_name": p.first_name,
        "last_name": p.last_name,
        "team": p.current_club_name,
        "position": p.position,
        "country_of_birth":p.country_of_birth
    } for p in players])


@app.route("/submit-name", methods=["POST"])
def submit_name():
    data = request.get_json()  # Get JSON data from request body
    if not data or "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400  # Return error if 'name' is missing

    name = data["name"]  # Extract name
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True)
