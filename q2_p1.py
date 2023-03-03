import pandas as pd
import numpy as np

df = pd.read_csv('country_vaccination_stats.csv')

country_min_vaccinations = df.groupby('country')['daily_vaccinations'].min()

df['imputed_daily_vaccinations'] = df.apply(lambda row: 
                                            country_min_vaccinations[row['country']] 
                                            if np.isnan(row['daily_vaccinations']) 
                                            else row['daily_vaccinations'], 
                                            axis=1)

df['imputed_daily_vaccinations'].fillna(0, inplace=True)

df.to_csv('vaccinations_imputed.csv', index=False)
