# 🍦 Ice Cream Sales Prediction Model

# 🚀 Live Deployment

🔗 https://icecream-sales-prediction-model-azure.onrender.com/

---
A sophisticated machine learning application that predicts ice cream sales based on weather conditions, day of week, and seasonal factors using **Linear Regression** and **Random Forest** models.

## ✨ Features

- **Dual ML Models**: Linear Regression and Random Forest algorithms for accurate predictions
- **Interactive Dashboard**: Beautiful, responsive web interface with real-time predictions
- **Monthly Analytics**: Visualize predicted sales across all 12 months
- **Weather Integration**: Temperature and rainfall impact analysis
- **Performance Metrics**: R² Score, MSE, and MAE for model evaluation
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Animated Visuals**: 5 colorful ice cream designs floating in the background

## 🎯 Key Statistics

| Metric | Linear Regression | Random Forest |
|--------|-------------------|---------------|
| **R² Score** | 0.9909 | **0.9979** ⭐ |
| **MSE** | 121 | **29** ⭐ |
| **MAE** | 9 | **4** ⭐ |

*Random Forest model demonstrates superior accuracy with lower error rates*

## 📊 Screenshots

### 🎨 Main Dashboard
![Dashboard](./docs/screenshots/dashboard.png)
**Input parameters form with real-time prediction results**
- Temperature and rainfall input fields
- Day of week and month selectors
- Beautiful gradient button with smooth animations
- Real-time Linear Regression & Random Forest predictions
- Clean, intuitive user interface

### 📈 Monthly Sales Predictions
![Graph](./docs/screenshots/monthly-predictions.png)
**Colorful bar chart showing predicted sales for all 12 months**
- Interactive bar chart with seasonal trends
- Each month displays different predicted sales value
- Multi-color design (pink, orange, yellow, mint, cyan)
- X-axis: All 12 months, Y-axis: Sales in units

### 📊 Model Performance Metrics
![Metrics](./docs/screenshots/model-metrics.png)
**Detailed performance comparison between both models**
- Linear Regression metrics: R² = 0.9909, MSE = 121, MAE = 9
- Random Forest metrics: R² = 0.9979, MSE = 29, MAE = 4
- Side-by-side comparison for easy evaluation
- Random Forest shows superior accuracy

> **Note:** To view screenshots, ensure the image files are uploaded to the `docs/screenshots/` folder. See [docs/README.md](./docs/README.md) for details.

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Local Installation

1. **Clone or navigate to the project directory:**
```bash
cd IceCream-Sales-Prediction-Model-Azure-master
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Flask application:**
```bash
python app.py
```

4. **Access the application:**
Open your browser and navigate to `http://localhost:5000`

## 🌐 Deployment to Render

### Step-by-Step Guide

1. **Create a GitHub Repository:**
   - Push all project files to GitHub (including Procfile)

2. **Sign up/Login to Render:**
   - Visit [render.com](https://render.com)
   - Sign in with your GitHub account

3. **Create a New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Give it a name (e.g., "ice-cream-sales-predictor")

4. **Configure Build & Start Commands:**

   **Build Command:**
   ```bash
   pip install -r requirements.txt
   ```

   **Start Command:**
   ```bash
   gunicorn app:app
   ```

5. **Select Plan:**
   - Choose Free tier ($0/month) or Starter plan
   - Click "Create Web Service"

6. **Wait for Deployment:**
   - Render will automatically build and deploy your app
   - You'll get a unique URL (e.g., `https://ice-cream-sales-predictor.onrender.com`)

### Environment Variables (if needed)
- `PORT`: Automatically set by Render (default: 5000)

## 📁 Project Structure

```
IceCream-Sales-Prediction-Model-Azure-master/
├── app.py                  # Flask application with ML models
├── index.html              # Interactive web interface
├── ice-cream.csv           # Training dataset (84 records)
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version specification
├── Procfile               # Render deployment configuration
└── README.md              # Project documentation
```

## 📦 Dependencies

```
Flask
gunicorn
pandas
numpy
scikit-learn
matplotlib
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Processing**: Pandas, NumPy
- **Visualization**: Chart.js
- **Deployment**: Gunicorn, Render

## 📈 How It Works

### Input Parameters
- **Temperature** (°F): 0-100°F range
- **Rainfall** (inches): 0-10 inches
- **Day of Week**: Monday through Sunday
- **Month**: January through December

### Prediction Process
1. User enters weather and temporal data
2. Features are encoded (categorical → numerical)
3. Both models generate predictions
4. Monthly sales graph is generated for all 12 months
5. Model performance metrics are displayed
6. Results shown with confidence indicators

## 🎓 Model Training

### Dataset
- **Records**: 84 entries covering full year cycle
- **Training/Test Split**: All data used for metrics calculation
- **Features**: Temperature, Rainfall, Day of Week, Month (encoded)

### Feature Engineering
- **DayOfWeek_encoded**: Label encoding (0-6)
- **Month_encoded**: Label encoding (0-11)
- Categorical values transformed for model compatibility

## 🔍 Example Usage

**Input:**
- Temperature: 98°F
- Rainfall: 2.90 inches
- Day: Friday
- Month: September

**Output:**
- Linear Regression Prediction: 989 units
- Random Forest Prediction: 693 units
- Monthly breakdown for all 12 months

## 📊 Data Analysis

### Seasonal Patterns
- **Peak Season**: June-August (higher temperatures, higher sales)
- **Low Season**: January-February (lower temperatures, lower sales)
- **Weather Impact**: Temperature has strong positive correlation with sales

### Day Effects
- Weekends typically show higher sales
- Consistent patterns across different months

## 💡 Recommendations

- **Use Random Forest predictions** for higher accuracy (R² = 0.9979)
- **Monitor weather forecasts** to anticipate demand changes
- **Plan inventory** based on monthly trend predictions
- **Adjust staffing** based on predicted high-demand periods

## 🐛 Troubleshooting

### Issue: Models not loading
**Solution**: Ensure `ice-cream.csv` is in the same directory as `app.py`

### Issue: Port already in use
**Solution**: Change port in `app.py` or stop other services using port 5000

### Issue: Module not found error
**Solution**: Install requirements: `pip install -r requirements.txt`

## 🔄 Updates & Maintenance

To retrain models with new data:
1. Update `ice-cream.csv` with new records
2. Restart Flask application
3. Models will automatically retrain on startup

## 📝 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📞 Support

For issues or questions, please create an issue in the GitHub repository.

---

**Made with ❤️ for ice cream lovers and data enthusiasts**

🍨 Deploy now and start predicting ice cream sales! 🍦
