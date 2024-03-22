import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


if __name__ == "__main__":
    df = load("./life_expectancy_years.csv")

    morocco = df.loc[df['country'] == 'Morocco']
    years = morocco.columns[1:]
    values = morocco.values[0][1:]
    plt.xticks(np.arange(0, 300, 40))
    plt.plot(np.array(years), np.array(values), label='Morocco')
    plt.title('Morocco Life expectancy Projections')
    plt.show()
