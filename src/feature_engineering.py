def add_features(df):
    # Extract hour
    df['Order_Hour'] = df['Order_Time'].dt.hour

    # Time slots
    def time_slot(hour):
        if hour < 12:
            return 'Morning'
        elif hour < 17:
            return 'Afternoon'
        elif hour < 21:
            return 'Evening'
        else:
            return 'Night'

    df['Time_Slot'] = df['Order_Hour'].apply(time_slot)

    return df