#Air Quality Prediction & AI Health Insight System

A full-stack machine learning project that predicts **PM2.5 air pollution levels** for Lucknow using real monitoring station data and provides **AI-generated health insights** using Google Gemini.

---

## 📌 Overview

This project uses historical air quality data from multiple monitoring stations in Lucknow to:

- Predict **PM2.5 concentration** using a trained ML regression model  
- Expose predictions via a **FastAPI backend**  
- Explain health impacts and pollutant risks using a **Gemini-powered LLM layer**  
- Visualize results through an interactive frontend  

The focus is on **end-to-end ML engineering**, not just model training.

---

## 🧠 System Architecture

Data (CSV files)
↓
Preprocessing & Cleaning
↓
Feature Engineering
↓
ML Model (Random Forest Regressor)
↓
FastAPI Backend
├── /predict → PM2.5 prediction
├── /insights → AI health explanation (Gemini)
└── /evaluation → Model metrics (RMSE, R²)
↓
Frontend (HTML/CSS/JS)


---

## 📊 Dataset

- Source: Government air quality monitoring stations  
- City: **Lucknow**  
- Time range used: **2019–2023**  
- Granularity: **Hourly data**  
- Multiple stations merged into a unified dataset  

Each station file contains pollutant concentrations such as:

- PM10  
- NO₂  
- SO₂  
- CO  
- Ozone  

along with timestamps and meteorological attributes.

---

## 🤖 Machine Learning Model

- **Model**: Random Forest Regressor  
- **Target**: PM2.5 concentration (µg/m³)  
- **Features used**:
  - PM10  
  - NO₂  
  - SO₂  
  - CO  
  - Ozone  
  - Month (seasonality)  

### 📈 Performance

- **R² score**: ~0.72  
- **RMSE**: ~33 µg/m³  

This reflects realistic performance on noisy, real-world environmental data.

---

## 🧠 AI Explainability (Gemini)

A separate LLM layer uses **Google Gemini** to:

- Interpret the predicted PM2.5 level  
- Categorize approximate AQI severity  
- Explain potential health effects  
- Highlight pollutants exceeding safe thresholds  

This keeps predictions **interpretable and user-focused**, rather than opaque numbers.

---

## 🚀 Backend (FastAPI)

### Available API Endpoints

- **POST `/predict`**  
  Returns predicted PM2.5 for given pollutant inputs.

- **POST `/insights`**  
  Returns AI-generated health and pollution impact explanation.

- **GET `/evaluation`**  
  Returns model evaluation metrics and feature importance.

CORS is enabled for frontend connectivity.

---

## 🖥️ Frontend

- Pure **HTML, CSS, and JavaScript**  
- Dynamic environment that changes with pollution severity  
- Visual AQI feedback + AI insights  
- No external frontend framework used  

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- FastAPI  
- Uvicorn  
- Google Gemini API  
- HTML, CSS, JavaScript  

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt

# Air Quality Prediction System

## 🚀 Getting Started

### 2. Run Backend

Start the FastAPI backend server with hot-reload enabled:

```bash
uvicorn backend.app:app --reload
```

### 3. Open Frontend

Open `index.html` in a browser. For better compatibility, serve it via a local server:

```bash
# Using Python's built-in server
python -m http.server 8000

# Or using Node.js http-server
npx http-server
```

Then navigate to `http://localhost:8000` in your browser.

## 🔐 Environment Variables

Set your Gemini API key before running the application:

**Linux/macOS:**
```bash
export GOOGLE_API_KEY=your_api_key_here
```

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

## 📌 Important Notes

- **Prediction Target**: The model predicts PM2.5 concentration values, not official AQI scores.
- **AQI Categories**: The displayed AQI categories are approximate and used only for interpretation purposes.
- **Project Focus**: This project prioritizes engineering workflow and model explainability over achieving perfect accuracy metrics.

## 🔍 Understanding the Output

The model provides PM2.5 predictions which are then mapped to AQI categories for easier interpretation:

| PM2.5 Range (µg/m³) | AQI Category |
|---------------------|--------------|
| 0-12 | Good |
| 12-35.4 | Moderate |
| 35.4-55.4 | Unhealthy for Sensitive Groups |
| 55.4-150.4 | Unhealthy |
| 150.4-250.4 | Very Unhealthy |
| 250.4+ | Hazardous |

---

For questions or issues, please refer to the project documentation or open an issue on GitHub.
