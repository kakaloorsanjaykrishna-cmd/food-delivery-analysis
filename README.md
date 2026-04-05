# 🍔 Online Food Delivery Data Analysis & Prediction System

## 🚀 Project Overview
This project is an end-to-end **Data Science + Machine Learning system** that analyzes food delivery data and predicts delivery time using advanced models.

It includes:
- 📊 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning (Random Forest)
- 🌐 Interactive Dashboard (Streamlit)

---

## 🎯 Key Features
- 📈 Data Analysis of orders, cuisines, delivery trends  
- 🚚 Delivery Time Prediction using ML  
- 🌦️ Feature-rich dataset (traffic, weather, weekend, festival)  
- 📊 Interactive graphs and filters  
- 💻 Streamlit dashboard for real-time prediction  

---

## 🧠 Machine Learning Model
- Algorithm: **Random Forest Regressor 🌲**
- Features used:
  - Distance
  - Order Value
  - Traffic Level
  - Weather
  - Vehicle Type
  - Weekend / Festival

### 📊 Performance
- **R² Score: ~0.89 🔥**
- **MSE: ~140**

---

## 🛠️ Tech Stack
- Python 🐍  
- Pandas, NumPy  
- Matplotlib  
- Scikit-learn  
- Streamlit  

---

## 📁 Project Structure
```
food-delivery-analysis/
│
├── src/                # Core ML logic
├── app/                # Streamlit dashboard
├── data/               # Dataset
├── models/             # Saved ML models
├── outputs/            # Graphs & reports
├── main.py             # Pipeline runner
├── generate_dataset.py # Dataset generator
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Clone Repository
```
git clone https://github.com/kakaloorsanjaykrishna-cmd/food-delivery-analysis.git
cd food-delivery-analysis
```

### 2. Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Generate Dataset
```
python generate_dataset.py
```

### 5. Run Full Pipeline
```
python main.py
```

### 6. Run Dashboard
```
streamlit run app/app.py
```

---

## 📊 Sample Insights
- 📅 Peak orders occur during evenings  
- 🚦 High traffic increases delivery time significantly  
- 🌧️ Weather impacts delivery performance  
- 📍 Distance strongly affects delivery time  

---


## 👨‍💻 Author
**Sanjay Krishna**  
- 🎓 B.Tech Student  
- 💻 Aspiring Software Engineer & Data Scientist  

---

## ⭐ If you like this project
Give it a ⭐ on GitHub and share it 🚀
