import pandas as pd
import numpy as np

df = pd.read_csv('country_vaccination_stats.csv')

df1 =  df[df['date']== '1/6/2021']

Total = df1['daily_vaccinations'].sum()

print(Total)