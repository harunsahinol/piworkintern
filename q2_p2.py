import pandas as pd
import numpy as np

df = pd.read_csv('country_vaccination_stats.csv')

highest_median_daily_vaccination = df.groupby('country')['daily_vaccinations'].median()

top_countries = highest_median_daily_vaccination.sort_values(ascending=False)

print(top_countries.head(3))




