import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import pandas as pd


if __name__ == "__main__":

    gross_domestic_product = load(
        "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")
    merge = pd.merge(gross_domestic_product[['country', '1900']],
                     life_expectancy[['country', '1900']], on='country',
                     suffixes=('_gdp', '_lf'))
    gdp = np.array(merge['1900_gdp'].values)
    lf = np.array(merge['1900_lf'].values)
    plt.scatter(gdp, lf)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()

