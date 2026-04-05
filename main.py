import os

from src.preprocess import clean_data
from src.feature_engineering import add_features
from src.train import train_model
from src.evaluate import evaluate_model
from src.eda import (
    plot_orders_by_day,
    plot_cuisine_distribution,
    plot_delivery_time
)

def ensure_folders():
    os.makedirs("models", exist_ok=True)
    os.makedirs("outputs/plots", exist_ok=True)
    os.makedirs("outputs/reports", exist_ok=True)

def run_pipeline():
    print("🚀 Starting Food Delivery ML Pipeline...\n")

    # Ensure folders exist
    ensure_folders()

    # Step 1: Load & Clean Data
    print("📥 Loading and cleaning data...")
    df = clean_data("data/raw/data.csv")

    # Step 2: Feature Engineering
    print("🧠 Adding features...")
    df = add_features(df)

    # Step 3: EDA (Graphs)
    print("📊 Generating graphs...")
    plot_orders_by_day(df)
    plot_cuisine_distribution(df)
    plot_delivery_time(df)

    # Step 4: Train Model
    print("🤖 Training model...")
    train_model(df)

    # Step 5: Evaluate Model
    print("📈 Evaluating model...")
    evaluate_model(df)

    print("\n✅ Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()