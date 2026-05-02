import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('suzuki_sales_data.csv')

# Sort by inflation for better visualization
df_sorted = df.sort_values(by='Inflation_Rate')

# Plot
plt.figure()
plt.plot(df_sorted['Inflation_Rate'], df_sorted['Sales_Units'])

plt.title('Impact of Inflation on Car Sales')
plt.xlabel('Inflation Rate (%)')
plt.ylabel('Sales Units')

# Save image
plt.savefig('dashboard_preview.png')

# Show plot
plt.show()

print("✅ dashboard_preview.png created!")