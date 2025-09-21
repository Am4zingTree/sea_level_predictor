import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # 1. Import data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # 3. Line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    plt.plot(years_all, intercept + slope * years_all, 'r', label='Fit All Data')

    # 4. Line of best fit for data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'],
                                                                           df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'green', label='Fit Since 2000')

    # 5. Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 6. Save plot
    plt.savefig('sea_level_plot.png')
    plt.show()


# Optional: run function for testing
if __name__ == "__main__":
    draw_plot()
