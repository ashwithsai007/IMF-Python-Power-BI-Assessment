import pandas as pd

# Input from Power BI
df = dataset

# Step 1: Standardize column names
df.columns = df.columns.str.strip()

# Step 2: Keep only necessary columns (Country, Subject Descriptor, and Year columns)
year_cols = [col for col in df.columns if str(col).isdigit()]
df = df[['Country', 'Subject Descriptor'] + year_cols]

# Step 3: Transform to long format
df_long = df.melt(
    id_vars=['Country', 'Subject Descriptor'],
    value_vars=year_cols,
    var_name='Year',
    value_name='Value'
)

# Step 4: Clean and convert data types
df_long['Year'] = df_long['Year'].astype(str)
df_long['Value'] = pd.to_numeric(df_long['Value'], errors='coerce')

# Step 5: Filter for relevant indicators only
indicators = ['Gross domestic product, constant prices', 'Inflation, average consumer prices']
df_filtered = df_long[df_long['Subject Descriptor'].isin(indicators)]

# Step 6: Pivot data for visualization
df_pivot = df_filtered.pivot_table(
    index=['Country', 'Year'],
    columns='Subject Descriptor',
    values='Value',
    aggfunc='mean'
).reset_index()

# Step 7: Rename pivoted columns
df_pivot.columns.name = None
df_pivot.rename(columns={
    'Gross domestic product, constant prices': 'GDP_Growth',
    'Inflation, average consumer prices': 'Inflation'
}, inplace=True)

# Ensure numeric types for visualization
df_pivot['GDP_Growth'] = pd.to_numeric(df_pivot['GDP_Growth'], errors='coerce')
df_pivot['Inflation'] = pd.to_numeric(df_pivot['Inflation'], errors='coerce')
df_pivot['Year'] = pd.to_numeric(df_pivot['Year'], errors='coerce')

# Step 8: Create summary table (average over time)
summary = df_pivot.groupby('Country', as_index=False).agg({
    'GDP_Growth': 'mean',
    'Inflation': 'mean'
}).round(2)

summary.rename(columns={
    'GDP_Growth': 'Avg_GDP_Growth',
    'Inflation': 'Avg_Inflation'
}, inplace=True)

# ✅ Return df_pivot for visualizations (line + bar charts)
df_pivot
import pandas as pd

# Input from Power BI
df = dataset

# Step 1: Standardize column names
df.columns = df.columns.str.strip()

# Step 2: Keep only necessary columns (Country, Subject Descriptor, and Year columns)
year_cols = [col for col in df.columns if str(col).isdigit()]
df = df[['Country', 'Subject Descriptor'] + year_cols]

# Step 3: Transform to long format
df_long = df.melt(
    id_vars=['Country', 'Subject Descriptor'],
    value_vars=year_cols,
    var_name='Year',
    value_name='Value'
)

# Step 4: Clean and convert data types
df_long['Year'] = df_long['Year'].astype(str)
df_long['Value'] = pd.to_numeric(df_long['Value'], errors='coerce')

# Step 5: Filter for relevant indicators only
indicators = ['Gross domestic product, constant prices', 'Inflation, average consumer prices']
df_filtered = df_long[df_long['Subject Descriptor'].isin(indicators)]

# Step 6: Pivot data for visualization
df_pivot = df_filtered.pivot_table(
    index=['Country', 'Year'],
    columns='Subject Descriptor',
    values='Value',
    aggfunc='mean'
).reset_index()

# Step 7: Rename pivoted columns
df_pivot.columns.name = None
df_pivot.rename(columns={
    'Gross domestic product, constant prices': 'GDP_Growth',
    'Inflation, average consumer prices': 'Inflation'
}, inplace=True)

# Ensure numeric types for visualization
df_pivot['GDP_Growth'] = pd.to_numeric(df_pivot['GDP_Growth'], errors='coerce')
df_pivot['Inflation'] = pd.to_numeric(df_pivot['Inflation'], errors='coerce')
df_pivot['Year'] = pd.to_numeric(df_pivot['Year'], errors='coerce')

# Step 8: Create summary table (average over time)
summary = df_pivot.groupby('Country', as_index=False).agg({
    'GDP_Growth': 'mean',
    'Inflation': 'mean'
}).round(2)

summary.rename(columns={
    'GDP_Growth': 'Avg_GDP_Growth',
    'Inflation': 'Avg_Inflation'
}, inplace=True)

df_pivot
