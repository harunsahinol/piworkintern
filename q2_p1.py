import pandas as pd
import numpy as np

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('country_vaccination_stats.csv')

# Group the data by country and find the minimum daily vaccinations per country
country_min_vaccinations = df.groupby('country')['daily_vaccinations'].min()

# Create a new column to store the imputed daily vaccinations
df['imputed_daily_vaccinations'] = df.apply(lambda row: 
                                            country_min_vaccinations[row['country']] 
                                            if np.isnan(row['daily_vaccinations']) 
                                            else row['daily_vaccinations'], 
                                            axis=1)

# Replace missing values with 0
df['imputed_daily_vaccinations'].fillna(0, inplace=True)

# Export the updated DataFrame to a new CSV file
df.to_csv('vaccinations_imputed.csv', index=False)
