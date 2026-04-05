import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)

num_rows = 3000

customer_types = ['New', 'Regular', 'Premium']
cuisines = ['Indian', 'Chinese', 'Italian', 'Fast Food', 'Desserts']
payment_methods = ['UPI', 'Card', 'Cash']
traffic_levels = ['Low', 'Medium', 'High']
weather_conditions = ['Clear', 'Rainy', 'Stormy']
vehicle_types = ['Bike', 'Scooter', 'Cycle']
delivery_statuses = ['On-Time', 'Late', 'Cancelled']

data = []

for i in range(num_rows):
    order_id = i + 1
    customer_id = random.randint(1000, 5000)
    customer_age = random.randint(18, 60)
    customer_type = random.choice(customer_types)

    restaurant_name = random.choice(['Spicy Hub', 'Urban Kitchen', 'Food Palace'])
    restaurant_rating = round(np.random.uniform(3.0, 5.0), 1)
    cuisine = random.choice(cuisines)

    order_value = round(np.random.uniform(150, 1200), 2)
    discount = round(np.random.uniform(0, 40), 2)
    payment_method = random.choice(payment_methods)

    distance = round(np.random.uniform(1, 15), 2)
    traffic = random.choice(traffic_levels)
    weather = random.choice(weather_conditions)

    partner_experience = round(np.random.uniform(0.5, 5), 1)
    vehicle = random.choice(vehicle_types)

    # Time
    start_date = datetime(2025, 1, 1)
    order_time = start_date + timedelta(minutes=random.randint(0, 60*24*90))
    day_of_week = order_time.strftime("%A")
    is_weekend = 1 if day_of_week in ['Saturday', 'Sunday'] else 0

    # Festival logic
    festival = 1 if random.random() < 0.1 else 0

    # Delivery time base
    delivery_time = distance * np.random.uniform(3, 5)

    # Traffic effect
    if traffic == 'High':
        delivery_time *= 1.5
    elif traffic == 'Medium':
        delivery_time *= 1.2

    # Weather effect
    if weather == 'Rainy':
        delivery_time *= 1.3
    elif weather == 'Stormy':
        delivery_time *= 1.6

    # Weekend / Festival effect
    if is_weekend:
        delivery_time *= 1.2
    if festival:
        delivery_time *= 1.4

    # Final adjustment
    delivery_time += np.random.uniform(5, 10)
    delivery_time = round(delivery_time, 2)

    late_delivery = 1 if delivery_time > 45 else 0

    # Delivery status
    if random.random() < 0.05:
        delivery_status = 'Cancelled'
    elif late_delivery:
        delivery_status = 'Late'
    else:
        delivery_status = 'On-Time'

    data.append([
        order_id, customer_id, customer_age, customer_type,
        restaurant_name, restaurant_rating, cuisine,
        order_value, discount, payment_method,
        distance, traffic, weather,
        delivery_time, late_delivery,
        partner_experience, vehicle,
        order_time, day_of_week, is_weekend,
        festival, delivery_status
    ])

df = pd.DataFrame(data, columns=[
    'Order_ID', 'Customer_ID', 'Customer_Age', 'Customer_Type',
    'Restaurant_Name', 'Restaurant_Rating', 'Cuisine',
    'Order_Value', 'Discount_Applied', 'Payment_Method',
    'Distance', 'Traffic_Level', 'Weather',
    'Delivery_Time', 'Late_Delivery',
    'Partner_Experience_Years', 'Vehicle_Type',
    'Order_Time', 'Day_of_Week', 'Is_Weekend',
    'Festival_Season', 'Delivery_Status'
])

df.to_csv("data/raw/data.csv", index=False)

print("🔥 Ultra dataset generated successfully!")