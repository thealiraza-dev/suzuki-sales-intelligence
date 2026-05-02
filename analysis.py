import pandas as pd

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("suzuki_sales_data.csv")

# -------------------------------
# BASIC KPI METRICS
# -------------------------------
total_sales = df["Sales_Units"].sum()
avg_sales = df["Sales_Units"].mean()

best_model = df.groupby("Model")["Sales_Units"].sum().idxmax()
best_city = df.groupby("City")["Sales_Units"].sum().idxmax()

print("\n==============================")
print("🚗 SUZUKI SALES BI REPORT")
print("==============================\n")

print(f"📦 Total Sales Units: {total_sales}")
print(f"📊 Average Sales per Record: {avg_sales:.2f}")
print(f"🏆 Best Performing Model: {best_model}")
print(f"🌍 Best Performing City: {best_city}")

# -------------------------------
# MODEL PERFORMANCE ANALYSIS
# -------------------------------
model_sales = df.groupby("Model")["Sales_Units"].sum().sort_values(ascending=False)

print("\n📊 Model Performance:")
print(model_sales)

# -------------------------------
# CITY PERFORMANCE ANALYSIS
# -------------------------------
city_sales = df.groupby("City")["Sales_Units"].sum().sort_values(ascending=False)

print("\n🌍 City Performance:")
print(city_sales)

# -------------------------------
# INFLATION IMPACT ANALYSIS
# -------------------------------
correlation = df["Inflation_Rate"].corr(df["Sales_Units"])

print("\n📉 Inflation Impact:")
print(f"Correlation between Inflation and Sales: {correlation:.2f}")

if correlation < 0:
    print("⚠️ Negative relationship detected: As inflation increases, sales decrease.")
else:
    print("📈 Positive relationship detected (unexpected in real market).")

# -------------------------------
# BUSINESS INSIGHT SUMMARY
# -------------------------------
print("\n🧠 Business Insights:")
print("- Focus marketing on top performing city.")
print("- Improve underperforming models.")
print("- Monitor inflation sensitivity in pricing strategy.")