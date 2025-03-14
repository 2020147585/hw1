import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

welfare = pd.read_csv("welfare.csv")
population = pd.read_csv("population_summary.csv")

welfare.rename(columns={'welfare of gdp': 'welfare_gdp_percentage'}, inplace=True)
population.rename(columns={'60+': 'above_60_population', '<60': 'under_60_population'}, inplace=True)

merged = welfare[['year', 'welfare_gdp_percentage']].merge(population, on="year")

merged['welfare_gdp_percentage'] = pd.to_numeric(merged['welfare_gdp_percentage'], errors='coerce').fillna(0)
merged['under_60_population'] = pd.to_numeric(merged['under_60_population'], errors='coerce').fillna(0)
merged['above_60_population'] = pd.to_numeric(merged['above_60_population'], errors='coerce').fillna(0)

sns.set_style("whitegrid")

fig, ax1 = plt.subplots(figsize=(12, 7))

bar1 = ax1.bar(merged['year'], merged['under_60_population'], color='blue', alpha=0.5, label="under 60")
bar2 = ax1.bar(merged['year'], merged['above_60_population'], color='red', alpha=0.5, bottom=merged['under_60_population'], label="above 60")
ax1.set_ylabel("Population", fontsize=14)
ax1.set_xlabel("Year", fontsize=14)

ax2 = ax1.twinx()
line, = ax2.plot(merged['year'], merged['welfare_gdp_percentage'], color='green', marker='o', linestyle='-', linewidth=2, label="Social welfare in GDP (%)")

ax2.set_yticks(merged['welfare_gdp_percentage'])
ax2.yaxis.grid(False)
ax2.set_ylabel("Social welfare in GDP (%)", fontsize=14)

handles = [bar1, bar2, line]
labels = ["under 60", "above 60", "Social welfare in GDP (%)"]
fig.legend(handles, labels, loc="upper right", fontsize=12, ncol=3, frameon=False)
plt.title("1970-2020 Growth in social welfare rate vs. Changes in the population aged under 60 & over 60", fontsize=18, pad=10)
plt.show()
