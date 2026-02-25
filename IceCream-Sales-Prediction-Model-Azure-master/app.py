from flask import Flask, request, jsonify, send_from_directory, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import os

app = Flask(__name__, static_folder='.', template_folder='.')

# ------------------ Utility Functions ------------------

def load_and_prepare_data(path='ice-cream.csv'):
    """Load CSV and encode categorical features."""
    df = pd.read_csv(path)
    le_day = LabelEncoder()
    le_month = LabelEncoder()
    df['DayOfWeek_encoded'] = le_day.fit_transform(df['DayOfWeek'])
    df['Month_encoded'] = le_month.fit_transform(df['Month'])
    return df, le_day, le_month


def train_models(df):
    """Train linear regression and random forest models."""
    features = ['Temperature', 'Rainfall', 'DayOfWeek_encoded', 'Month_encoded']
    X = df[features]
    y = df['IceCreamsSold']

    lr = LinearRegression().fit(X, y)
    rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1).fit(X, y)
    return lr, rf


# ------------------ Load Data & Train Models ------------------

DATA_PATH = 'ice-cream.csv'   # CSV must be in root directory

try:
    df, le_day, le_month = load_and_prepare_data(DATA_PATH)
    model_lr, model_rf = train_models(df)
    print("Models loaded successfully")
except Exception as e:
    df, le_day, le_month, model_lr, model_rf = None, None, None, None, None
    print(f"Startup Error: {e}")


# ------------------ Routes ------------------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def get_data():
    return send_from_directory('.', 'ice-cream.csv')


@app.route('/api/predict', methods=['POST'])
def predict():

    if model_lr is None or model_rf is None:
        return jsonify({'error': 'Models not available'}), 500

    payload = request.get_json(force=True)

    try:
        temp = float(payload['temperature'])
        rain = float(payload['rainfall'])
        day = payload['dayOfWeek']
        month = payload['month']
    except KeyError as ke:
        return jsonify({'error': f'Missing field {ke}'}), 400

    day_enc = int(le_day.transform([day])[0])
    mon_enc = int(le_month.transform([month])[0])

    X = np.array([[temp, rain, day_enc, mon_enc]])

    pred_lr = model_lr.predict(X)[0]
    pred_rf = model_rf.predict(X)[0]

    return jsonify({
        'linear_regression': max(0, float(pred_lr)),
        'random_forest': max(0, float(pred_rf))
    })


@app.route('/api/metrics')
def get_metrics():

    if df is None:
        return jsonify({'error': 'Data not available'}), 500

    features = ['Temperature', 'Rainfall', 'DayOfWeek_encoded', 'Month_encoded']
    X = df[features]
    y = df['IceCreamsSold']

    y_pred_lr = model_lr.predict(X)
    y_pred_rf = model_rf.predict(X)

    def metrics(y_true, y_pred):
        mse = np.mean((y_true - y_pred) ** 2)
        mae = np.mean(np.abs(y_true - y_pred))
        r2 = 1 - np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
        return {'r2': float(r2), 'mse': float(mse), 'mae': float(mae)}

    return jsonify({
        'linear_regression': metrics(y, y_pred_lr),
        'random_forest': metrics(y, y_pred_rf)
    })


@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)


# ------------------ Render Port Binding ------------------

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)