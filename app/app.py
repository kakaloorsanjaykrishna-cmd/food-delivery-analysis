import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -------------------------------
# Load Data & Model
# -------------------------------
df = pd.read_csv("data/raw/data.csv")
model = joblib.load("models/delivery_model.pkl")

st.set_page_config(page_title="🍔 Food Delivery Dashboard", layout="wide")

st.title("🍔 Online Food Delivery Analysis & Prediction")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

cuisine = st.sidebar.selectbox("Cuisine", df['Cuisine'].unique())
traffic = st.sidebar.selectbox("Traffic Level", df['Traffic_Level'].unique())
weather = st.sidebar.selectbox("Weather", df['Weather'].unique())

filtered_df = df[
    (df['Cuisine'] == cuisine) &
    (df['Traffic_Level'] == traffic) &
    (df['Weather'] == weather)
]

# -------------------------------
# SHOW DATA
# -------------------------------
st.subheader("📊 Filtered Data")
st.dataframe(filtered_df.head(10))

# -------------------------------
# GRAPH 1: Orders by Day
# -------------------------------
st.subheader("📅 Orders by Day")

fig1, ax1 = plt.subplots()
filtered_df['Day_of_Week'].value_counts().plot(kind='bar', ax=ax1)
ax1.set_title("Orders Distribution")
st.pyplot(fig1)

# -------------------------------
# GRAPH 2: Delivery Time vs Distance
# -------------------------------
st.subheader("🚚 Delivery Time vs Distance")

fig2, ax2 = plt.subplots()
ax2.scatter(filtered_df['Distance'], filtered_df['Delivery_Time'])
ax2.set_xlabel("Distance")
ax2.set_ylabel("Delivery Time")
st.pyplot(fig2)

# -------------------------------
# GRAPH 3: Cuisine Popularity
# -------------------------------
st.subheader("🍽️ Cuisine Distribution")

fig3, ax3 = plt.subplots()
df['Cuisine'].value_counts().plot(kind='bar', ax=ax3)
st.pyplot(fig3)

# -------------------------------
# 🎯 PREDICTION SECTION
# -------------------------------
st.subheader("🎯 Predict Delivery Time")

col1, col2 = st.columns(2)

with col1:
    distance = st.number_input("Distance (km)", 1.0, 20.0, 5.0)
    order_value = st.number_input("Order Value", 100.0, 2000.0, 500.0)
    discount = st.number_input("Discount (%)", 0.0, 50.0, 10.0)

with col2:
    traffic_input = st.selectbox("Traffic", df['Traffic_Level'].unique())
    weather_input = st.selectbox("Weather", df['Weather'].unique())
    vehicle = st.selectbox("Vehicle Type", df['Vehicle_Type'].unique())

is_weekend = st.selectbox("Weekend?", [0, 1])
festival = st.selectbox("Festival?", [0, 1])

# -------------------------------
# PREPARE INPUT (IMPORTANT 🔥)
# -------------------------------
def prepare_input():
    input_dict = {
        'Distance': distance,
        'Order_Value': order_value,
        'Discount_Applied': discount,
        'Is_Weekend': is_weekend,
        'Festival_Season': festival,
        'Traffic_Level': traffic_input,
        'Weather': weather_input,
        'Vehicle_Type': vehicle
    }

    input_df = pd.DataFrame([input_dict])

    # Combine with training data columns
    temp_df = pd.concat([df, input_df], ignore_index=True)

    temp_df = pd.get_dummies(temp_df, drop_first=True)

    input_final = temp_df.tail(1)

    return input_final

# -------------------------------
# PREDICT BUTTON
# -------------------------------
if st.button("🚀 Predict Delivery Time"):
    input_data = prepare_input()
    prediction = model.predict(input_data)

    st.success(f"⏱️ Estimated Delivery Time: {prediction[0]:.2f} minutes")