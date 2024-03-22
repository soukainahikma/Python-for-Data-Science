import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def convert_population(population):
    suffix = population[-1]
    if suffix == 'M':
        return float(population[:-1]) * 1e6
    elif suffix == 'K':
        return float(population[:-1]) * 1e3
    elif suffix == 'B':
        return float(population[:-1]) * 1e9
    else:
        return float(population)


def ft_plot_countries(df):
    df['France'] = df['France'].apply(convert_population)
    df['Morocco'] = df['Morocco'].apply(convert_population)

    df.reset_index(inplace=True)

    plt.figure(figsize=(10, 6))
    df = df[(df['index'].astype(int) >= 1800) &
            (df['index'].astype(int) <= 2050)]
    plt.plot(df['index'].values, df['France'].values, label='France')

    plt.plot(df['index'].values, df['Morocco'].values, label='Morocco')

    ticks = np.arange(0, 241, 40)
    labels = ['20M', '40M', '60M']
    xlabels = ["1800", "1840", "1880", "1920", "1960", "2000", "2040"]
    plt.yticks(np.arange(20*1e6, 61*1e6, 20*1e6), labels)
    plt.xticks(ticks, xlabels)
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.show()


if __name__ == "__main__":

    df = load("./population_total.csv")
    df.set_index(["country"], inplace=True)
    df_T = df.T
    ft_plot_countries(df_T)
