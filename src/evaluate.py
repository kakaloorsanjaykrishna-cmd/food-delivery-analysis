import joblib
import pandas as pd

from sklearn.metrics import r2_score, mean_squared_error


def evaluate_model(df):
    print("📈 Evaluating model...")

    # Same features as training 🔥
    features = [
        'Distance', 'Order_Value', 'Discount_Applied',
        'Traffic_Level', 'Weather', 'Vehicle_Type',
        'Is_Weekend', 'Festival_Season'
    ]

    df = df[features + ['Delivery_Time']]

    # Convert categorical → numeric
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop('Delivery_Time', axis=1)
    y = df['Delivery_Time']

    # Load model (FIXED NAME ✅)
    model = joblib.load("models/delivery_model.pkl")

    # Predict
    y_pred = model.predict(X)

    print("\n📊 Evaluation Results:")
    print("R2 Score:", r2_score(y, y_pred))
    print("MSE:", mean_squared_error(y, y_pred))