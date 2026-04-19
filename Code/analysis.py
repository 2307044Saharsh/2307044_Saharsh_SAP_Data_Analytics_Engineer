import pandas as pd
import os
# Load files
houses = pd.read_csv('Data/households.csv')
usage = pd.read_csv('Data/electricity_usage.csv')

# Merge
merged = usage.merge(houses, on='house_id')

# Create Output folder
os.makedirs('Output', exist_ok=True)

# Highest consumption by house
highest_consumption = merged.groupby('house_name')['units_consumed'].sum().reset_index()
highest_consumption.columns = ['House Name', 'Total Units']
highest_consumption = highest_consumption.sort_values('Total Units', ascending=False)

# Monthly trend
monthly_trend = merged.groupby('month')['units_consumed'].sum().reset_index()
monthly_trend.columns = ['Month', 'Total Units']

# Average usage
average_usage = merged.groupby('house_name')['units_consumed'].mean().reset_index()
average_usage.columns = ['House Name', 'Average Units']

# Save output CSVs
highest_consumption.to_csv('Output/highest_consumption.csv', index=False)
monthly_trend.to_csv('Output/monthly_trend.csv', index=False)
average_usage.to_csv('Output/average_usage.csv', index=False)

print(highest_consumption)
print(monthly_trend)
print(average_usage)