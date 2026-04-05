import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


def train_model(df):
    print("🚀 Training Advanced Model (Random Forest)...")

    # 🔥 Feature selection
    features = [
        'Distance', 'Order_Value', 'Discount_Applied',
        'Traffic_Level', 'Weather', 'Vehicle_Type',
        'Is_Weekend', 'Festival_Season'
    ]

    df = df[features + ['Delivery_Time']]

    # Convert categorical → numeric
    df = pd.get_dummies(df, drop_first=True)

    # Split
    X = df.drop('Delivery_Time', axis=1)
    y = df['Delivery_Time']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 🌲 Model
    model = RandomForestRegressor(
        n_estimators=120,
        max_depth=12,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    print("\n📊 Training Performance:")
    print("R2 Score:", r2_score(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))

    # Save model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/delivery_model.pkl")

    print("\n✅ Model saved at models/delivery_model.pkl")

    return model


# ▶️ Run directly
if __name__ == "__main__":
    from src.preprocess import clean_data
    from src.feature_engineering import add_features

    df = clean_data("data/raw/data.csv")
    df = add_features(df)

    train_model(df)