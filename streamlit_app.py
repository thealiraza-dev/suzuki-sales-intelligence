import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Suzuki Sales Intelligence",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("suzuki_sales_data.csv")

# -------------------------------
# HEADER
# -------------------------------
st.title("🚗 Suzuki Sales Intelligence Dashboard")
st.caption("Business Intelligence system for sales, inflation & regional analysis")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

model_filter = st.sidebar.multiselect(
    "Select Model",
    df["Model"].unique(),
    default=df["Model"].unique()
)

city_filter = st.sidebar.multiselect(
    "Select City",
    df["City"].unique(),
    default=df["City"].unique()
)

filtered_df = df[
    (df["Model"].isin(model_filter)) &
    (df["City"].isin(city_filter))
]

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# -------------------------------
# KPI SECTION
# -------------------------------
total_sales = filtered_df["Sales_Units"].sum()
avg_sales = filtered_df["Sales_Units"].mean()
best_model = filtered_df.groupby("Model")["Sales_Units"].sum().idxmax()
best_city = filtered_df.groupby("City")["Sales_Units"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", total_sales)
col2.metric("Avg Sales", round(avg_sales, 2))
col3.metric("Top Model", best_model)
col4.metric("Top City", best_city)

# -------------------------------
# CHART 1: MODEL PERFORMANCE
# -------------------------------
st.subheader("📊 Model Performance")
fig1, ax1 = plt.subplots()
filtered_df.groupby("Model")["Sales_Units"].sum().plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# -------------------------------
# CHART 2: CITY PERFORMANCE
# -------------------------------
st.subheader("🌍 City Performance")
fig2, ax2 = plt.subplots()
filtered_df.groupby("City")["Sales_Units"].sum().plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# -------------------------------
# CHART 3: INFLATION VS SALES
# -------------------------------
st.subheader("📉 Inflation vs Sales Relationship")
fig3, ax3 = plt.subplots()
ax3.scatter(filtered_df["Inflation_Rate"], filtered_df["Sales_Units"])
ax3.set_xlabel("Inflation Rate")
ax3.set_ylabel("Sales Units")
st.pyplot(fig3)

# -------------------------------
# INSIGHTS SECTION
# -------------------------------
st.subheader("🧠 Business Insights")

correlation = filtered_df["Inflation_Rate"].corr(filtered_df["Sales_Units"])

st.write(f"📉 Inflation-Sales Correlation: **{correlation:.2f}**")

if correlation < 0:
    st.error("Inflation negatively impacts sales. Pricing strategy adjustment needed.")
else:
    st.success("Sales are not strongly affected by inflation in this dataset.")

st.write("✔ Focus on top-performing city for expansion")
st.write("✔ Improve marketing for underperforming models")
st.write("✔ Monitor inflation sensitivity for pricing strategy")

# -------------------------------
# RAW DATA VIEW
# -------------------------------
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)