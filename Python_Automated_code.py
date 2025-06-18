import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter

# === Load the dataset ===
print("Reading the IMF dataset...")
file_path = r"C:\Users\LENOVO\Desktop\Data.xlsx"
raw_data = pd.read_excel(file_path)

# Keep only what's needed: country, indicator, and yearly values
important_columns = ['Country', 'Subject Descriptor'] + list(range(2015, 2025))
clean_data = raw_data[important_columns].copy()

# Convert from wide to long format
print("Transforming data into long format...")
long_format = clean_data.melt(
    id_vars=['Country', 'Subject Descriptor'],
    var_name='Year',
    value_name='Value'
)

# Fix data types
long_format['Year'] = long_format['Year'].astype(int)
long_format['Value'] = pd.to_numeric(long_format['Value'], errors='coerce')

# Create a pivot where each row is a country-year and columns are indicators
print("Creating pivot table...")
wide_data = long_format.pivot_table(
    index=['Country', 'Year'],
    columns='Subject Descriptor',
    values='Value'
).reset_index()

# Clean up column names for easier access
wide_data.columns.name = None
wide_data.rename(columns={
    'Gross domestic product, constant prices': 'GDP_Growth',
    'Inflation, average consumer prices': 'Inflation'
}, inplace=True)

# === Summarize: average GDP growth and inflation per country ===
print("Calculating 10-year averages...")
summary_table = wide_data.groupby('Country').agg({
    'GDP_Growth': 'mean',
    'Inflation': 'mean'
}).round(2).reset_index()

summary_table.rename(columns={
    'GDP_Growth': 'Avg_GDP_Growth',
    'Inflation': 'Avg_Inflation'
}, inplace=True)

# === Plotting charts ===
# GDP Line Chart
print("Plotting GDP growth chart...")
plt.figure(figsize=(8, 5))
for nation in wide_data['Country'].unique():
    gdp_values = wide_data[wide_data['Country'] == nation]
    plt.plot(gdp_values['Year'], gdp_values['GDP_Growth'], marker='o', label=nation)
plt.title('GDP Growth Over Time (2015–2024)')
plt.xlabel('Year')
plt.ylabel('% GDP Growth')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('gdp_growth_linechart.png')
plt.close()

# Inflation bar chart for 2024
print("Plotting inflation chart for 2024...")
inflation_2024 = wide_data[wide_data['Year'] == 2024]
plt.figure(figsize=(6, 4))
plt.bar(inflation_2024['Country'], inflation_2024['Inflation'], color='orange')
plt.title('Inflation Rates in 2024')
plt.xlabel('Country')
plt.ylabel('% Inflation')
plt.tight_layout()
plt.savefig('inflation_2024_barchart.png')
plt.close()

# === Export everything to Excel ===
print("Writing summary and charts to Excel...")
output_file = 'IMF_Summary_Report.xlsx'
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    book = writer.book
    sheet = book.add_worksheet('Summary')
    writer.sheets['Summary'] = sheet

    # Write summary table to Excel
    summary_table.to_excel(writer, sheet_name='Summary', startrow=0, startcol=0, index=False)

    # Add charts
    sheet.insert_image('E2', 'gdp_growth_linechart.png')
    sheet.insert_image('E20', 'inflation_2024_barchart.png')

print("Done! Excel file saved as:", output_file)
