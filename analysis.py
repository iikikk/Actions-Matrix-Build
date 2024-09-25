import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reads dataset
file_path = 'TFL Bus Safety.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

print("First few rows of the dataset:")
print(data.head())

print("\nData types of each column:")
print(data.dtypes)

# Summary statistics
statistics = data.describe(include='all')
print(statistics)

year_stats = data['Year'].agg(['mean', 'median', 'std'])
print(f" Summary Statistics for Year:\n{year_stats}")