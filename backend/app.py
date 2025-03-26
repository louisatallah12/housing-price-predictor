from flask import Flask, request, jsonify
from flask_cors import CORS 
import joblib
import sqlite3

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load('backend/models/model.pkl')

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('backend/database/predictions.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    sqft = data.get('sqft')
    bedrooms = data.get('bedrooms')

    if not sqft or not bedrooms:
        return jsonify({"error": "Missing required fields"}), 400

    prediction = model.predict([[sqft, bedrooms]])[0]

    # Store in database
    conn = get_db_connection()
    conn.execute("INSERT INTO predictions (sqft, bedrooms, predicted_price) VALUES (?, ?, ?)", 
                 (sqft, bedrooms, prediction))
    conn.commit()
    conn.close()

    return jsonify({'predicted_price': round(prediction, 2)})

if __name__ == '__main__':
    app.run(debug=True)
