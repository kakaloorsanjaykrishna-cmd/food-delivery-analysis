import pandas as pd

def clean_data(path):
    df = pd.read_csv(path)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.dropna(inplace=True)

    # Convert datetime
    df['Order_Time'] = pd.to_datetime(df['Order_Time'])

    return df