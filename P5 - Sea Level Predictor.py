import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", sep=",", header=0)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", color="#139DB9")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = list(range(df["Year"].min(), 2051))
    y_pred = [slope * x + intercept for x in x_pred]
    plt.plot(x_pred, y_pred, label="Line of Best Fit (1880-2050)", color="#B91713")

    # Create second line of best fit
    recent_data = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"])
    x_pred_recent = list(range(recent_data["Year"].min(), 2051))
    y_pred_recent = [slope_recent * x + intercept_recent for x in x_pred_recent]
    plt.plot(x_pred_recent, y_pred_recent, label="Line of Best Fit (2000-2050)", color="#006600")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
plt.show()
