# Systems-Engineer-Position-Assignment

# 📊 GDP & Inflation Analysis with Python in Power BI

Hi! This is a Python script I used inside Power BI to clean and analyze a dataset that has GDP growth and inflation data for different countries from 2015 to 2024. The script helps turn messy economic data into clean visuals and summary tables that are ready to use in dashboards.

---

## 🔧 How to Use This Script in Power BI

### ✅ Step-by-step:

1. Open Power BI Desktop.
2. Click **Get Data → Excel** or **CSV**, and load your dataset.
3. Go to **Home → Transform Data**.
4. In the Power Query Editor, click on **Run Python Script**.
5. Paste the entire script from `gdp_inflation_analysis_powerbi.py`.
6. Click OK → then **Close & Apply**.

> ⚠️ Important: You must have Python installed on your computer and set up in Power BI.  
> Go to **File → Options → Python scripting**, and choose your Python installation (Anaconda or standard Python).

---

## 🐍 What the Python Script Does

Here’s a simple breakdown of what the script is doing:

1. **Cleans the data**  
   - Removes unnecessary columns like "Units", "Scale", and notes
   - Keeps only columns like `Country`, `Subject Descriptor`, and years

2. **Transforms it**  
   - Converts wide format (many year columns) into long format (one column for year)
   - Filters for just two indicators:
     - GDP Growth (`Gross domestic product, constant prices`)
     - Inflation (`Inflation, average consumer prices`)

3. **Creates two new tables**  
   - `df_pivot`: Ready for charts, with columns for `Country`, `Year`, `GDP_Growth`, and `Inflation`
   - `summary`: Averages for each country over the full period (2015–2024)

---

## 📈 Charts You Can Create in Power BI

### 1. **Line Chart – GDP Growth Over Time**

- Visual type: **Line Chart**
- X-axis: `Year`
- Y-axis: `GDP_Growth`
- Legend: `Country`
- Make sure the `Year` column is set as a **Whole Number** or **Continuous**

### 2. **Bar Chart – Inflation in 2024**

- Visual type: **Clustered Column Chart**
- Add filter: `Year = 2024`
- X-axis: `Country`
- Y-axis: `Inflation`
- Sort by `Inflation` descending for better comparison

---

## 📊 Summary Table

The script also gives you a `summary` table that shows:

| Country       | Avg_GDP_Growth | Avg_Inflation |
|---------------|----------------|----------------|
| India         | 6.25           | 5.31           |
| USA           | 2.45           | 2.88           |
| Germany       | 1.12           | 2.17           |

You can use this table to compare long-term trends and spot high-growth or high-inflation countries.

---

## 💬 How to Interpret the Charts

- A **rising GDP growth line** shows positive economic performance.
- A **high inflation bar** in 2024 might indicate economic pressure or cost-of-living increases.
- The **summary table** helps see which countries were more stable or volatile over 10 years.

---

## 📁 Files Included

- `gdp_inflation_analysis_powerbi.py` – Python script for cleaning and processing
- `README.md` – This instruction file
- *(Optional)* `df_pivot.csv` and `summary.csv` if exported from Power BI

---

## ✅ Final Tips

- If you can’t see lines in the chart, make sure `GDP_Growth` and `Year` are numeric types.
- You can add a slicer for `Country` or `Year` to make the visuals more interactive.
- Only one table (like `df_pivot` or `summary`) can be returned at a time from a Python script in Power BI. Just switch the last line of code accordingly.

---

Thanks for checking this out! Let me know if you want help formatting the dashboard or exporting to Excel with charts 📈📤
