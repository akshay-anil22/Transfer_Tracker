import pandas as pd
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import numpy as np


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Database configuration
DB_USER = "root"
DB_PASSWORD = "akshay@1324"
DB_HOST = "localhost"
DB_NAME = "transfertracker"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:akshay%401324@localhost:3306/transfertracker"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Player model
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

# Function to insert data from Excel
def insert_data_from_excel(excel_file):
    
    df = pd.read_csv(excel_file)
    df = df.replace({np.nan: None})

    for _, row in df.iterrows():
        player = Player(
            player_id=row["player_id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            name=row["name"],
            last_season=row["last_season"],
            current_club_id=row["current_club_id"],
            player_code=row["player_code"],
            country_of_birth=row["country_of_birth"],
            country_of_citizenship=row["country_of_citizenship"],
            date_of_birth = (
    pd.to_datetime(row["date_of_birth"], format="%d-%m-%Y %H:%M", dayfirst=True).date()
    if pd.notna(row["date_of_birth"]) else None
)
,
            sub_position=row["sub_position"],
            position=row["position"],
            foot=row["foot"],
            height_in_cm=row["height_in_cm"],
            contract_expiration_date = (
    pd.to_datetime(row["contract_expiration_date"], format="%d-%m-%Y %H:%M", dayfirst=True).date()
    if pd.notnull(row["contract_expiration_date"])
    else None
),
            agent_name=row["agent_name"],
            image_url=row["image_url"],
            url=row["url"],
            current_club_domestic_competition_id=row["current_club_domestic_competition_id"],
            current_club_name=row["current_club_name"],
            market_value_in_eur=row["market_value_in_eur"],
            highest_market_value_in_eur=row["highest_market_value_in_eur"]
        )
        db.session.add(player)

    db.session.commit()
    print("✅ Data inserted successfully from Excel!")

# API route to fetch all players
@app.route('/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    players_list = [
        {
            "player_id": player.player_id,
            "name": player.name,
            "position": player.position,
            "current_club_name": player.current_club_name,
            "market_value_in_eur": player.market_value_in_eur,
            "image_url": player.image_url
        }
        for player in players
    ]
    return jsonify(players_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database tables are created

        # Insert data from Excel (Change the path if your file is elsewhere)
        excel_path = "C:/Users/aksha/OneDrive/Desktop/Transfer_Tracker/players4.csv"  # 🔹 Updated file path
        insert_data_from_excel(excel_path)

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port) 