# Housing price predictor


## Backend (Flask API - Python)

cd backend
pip install -r requirements.txt
python models/train_model.py
python database/init_db.py
python app.py

### The server is listening on port 5000

## Frontend (React)

### Replace the environment variable at the root to add the address of the server (API URL)
npm install
npm start

### The frontend will now run at http://{localhost}:3000


## Database (sqlite)
### View results in database

sqlite3 backend/database/predictions.db
select * from predictions;

### Predictions are also stored in predictions.db