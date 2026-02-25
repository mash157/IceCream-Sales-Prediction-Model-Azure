# 📸 Documentation & Screenshots

## Project Screenshots

This folder contains all documentation and visual assets for the Ice Cream Sales Prediction Model project.

### Folder Structure

```
docs/
├── screenshots/
│   ├── dashboard.png           # Main dashboard with input form & predictions
│   ├── monthly-predictions.png # Monthly sales bar chart
│   └── model-metrics.png       # Model performance metrics
└── README.md                   # This file
```

## Adding Screenshots

To add your project screenshots:

1. Take or save screenshots of:
   - **dashboard.png**: Show the input parameters form with prediction results
   - **monthly-predictions.png**: Show the monthly sales graph with all 12 months
   - **model-metrics.png**: Show the model performance metrics section

2. Place them in the `screenshots/` subfolder

3. The README.md will automatically reference them as:
   ```markdown
   ![Dashboard](./docs/screenshots/dashboard.png)
   ```

## Screenshots Overview

### 1. Dashboard (dashboard.png)
- Input form with Temperature, Rainfall, Day of Week, and Month selectors
- Real-time prediction results showing both Linear Regression and Random Forest predictions
- Beautiful gradient button with hover effects
- Clean user interface with pink and orange color scheme

### 2. Monthly Predictions (monthly-predictions.png)
- Interactive bar chart showing predicted sales for all 12 months
- Colorful bars (pink, orange, yellow, mint green, cyan)
- X-axis shows all months (January-December)
- Y-axis shows predicted sales in units
- Legend indicating "Predicted Sales (units)"

### 3. Model Metrics (model-metrics.png)
- Side-by-side comparison of Linear Regression and Random Forest models
- Metrics displayed: R² Score, MSE (Mean Squared Error), MAE (Mean Absolute Error)
- Each metric in a separate card with pink borders
- Shows Random Forest's superior performance (R² = 0.9979 vs 0.9909)

## Visual Design

- **Color Scheme**: Warm pastels (Pink, Orange, Yellow, Mint, Cyan)
- **Background**: Animated gradient with floating ice cream designs
- **Components**: Rounded cards, smooth transitions, hover effects
- **Responsive**: Works on desktop and mobile devices

---

*Add your screenshots to the `screenshots/` folder and ensure the main README.md references them correctly.*
