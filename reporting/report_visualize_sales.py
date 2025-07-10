import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#  Locate the cleaned CSV
project_root = os.path.dirname(os.path.dirname(__file__))  # Go up from /reporting/
csv_path = os.path.join(project_root, "etl_clean", "cleaned_sales_data.csv")

#  Load cleaned data with proper datetime parsing
df = pd.read_csv(csv_path, parse_dates=["sale_date"])
df["sale_date"] = pd.to_datetime(df["sale_date"])  # Ensure it's datetime

#  Output directory (same as script location)
output_dir = os.path.dirname(__file__)
os.makedirs(output_dir, exist_ok=True)

#  Sales by Region (Bar Chart)
region_summary = df.groupby("region")["total_sales"].sum().sort_values()

plt.figure(figsize=(8, 5))
sns.barplot(
    x=region_summary.values,
    y=region_summary.index,
    hue=region_summary.index,
    palette="mako",
    legend=False
)
plt.title("Total Sales by Region")
plt.xlabel("Sales")
plt.tight_layout()

region_chart_path = os.path.join(output_dir, "sales_by_region.png")
plt.savefig(region_chart_path)
plt.close()
print("Saved chart:", region_chart_path)

# 🔹 Monthly Sales Trend (Line Chart)
monthly_sales = df.resample("M", on="sale_date")["total_sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker='o', color='teal')
plt.title("Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()

monthly_chart_path = os.path.join(output_dir, "monthly_sales_trend.png")
plt.savefig(monthly_chart_path)
plt.close()
print("Saved chart:", monthly_chart_path)
