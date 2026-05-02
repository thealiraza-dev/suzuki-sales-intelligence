import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    'Region': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore'],
    'Sales': [200, 150, 100, 250, 300]
}

df = pd.DataFrame(data)

# Group by region
region_sales = df.groupby('Region')['Sales'].sum()

# Print result
print(region_sales)

# Plot chart
region_sales.plot(kind='bar')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()