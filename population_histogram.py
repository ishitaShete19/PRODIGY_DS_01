import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_2590.csv', skiprows=4)

# Filter for year 2023 and remove non-country entries
df_2023 = df[['Country Name', '2023']].dropna()

# Remove aggregate regions (non-countries)
non_countries = [
    "World", "High income", "Low income", "Middle income", "OECD members",
    "Arab World", "Europe & Central Asia", "Sub-Saharan Africa",
    "East Asia & Pacific", "North America", "South Asia",
    "Latin America & Caribbean", "European Union", "Least developed countries"
]
df_2023 = df_2023[~df_2023['Country Name'].isin(non_countries)]

# Convert population to millions for readability
df_2023['2023'] = df_2023['2023'] / 1e6

# Plot histogram of population distribution
plt.figure(figsize=(10, 6))
plt.hist(df_2023['2023'], bins=20, color='teal', edgecolor='black')
plt.title('Histogram of Country Populations in 2023', fontsize=14)
plt.xlabel('Population (in millions)')
plt.ylabel('Number of Countries')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('population_histogram_2023.png')
plt.show()
