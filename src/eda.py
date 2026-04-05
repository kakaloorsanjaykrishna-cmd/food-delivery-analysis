import matplotlib.pyplot as plt

def plot_orders_by_day(df):
    df['Day_of_Week'].value_counts().plot(kind='bar')
    plt.title("Orders by Day")
    plt.savefig("outputs/plots/orders_by_day.png")
    plt.clf()

def plot_cuisine_distribution(df):
    df['Cuisine'].value_counts().plot(kind='bar')
    plt.title("Cuisine Distribution")
    plt.savefig("outputs/plots/cuisine_distribution.png")
    plt.clf()

def plot_delivery_time(df):
    plt.scatter(df['Distance'], df['Delivery_Time'])
    plt.xlabel("Distance")
    plt.ylabel("Delivery Time")
    plt.title("Delivery Time vs Distance")
    plt.savefig("outputs/plots/delivery_time_vs_distance.png")
    plt.clf()