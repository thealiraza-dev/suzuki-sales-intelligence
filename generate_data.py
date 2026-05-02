import pandas as pd
import random
from datetime import datetime, timedelta

# Settings
num_rows = 500
models = ['Alto', 'Swift', 'Cultus']
cities = ['Karachi', 'Lahore', 'Islamabad']

# Generate dates
start_date = datetime(2022, 1, 1)

data = []

for i in range(num_rows):
    date = start_date + timedelta(days=i)
    model = random.choice(models)
    city = random.choice(cities)

    inflation_rate = round(random.uniform(5, 25), 2)

    # Sales drop when inflation increases (simple logic)
    base_sales = random.randint(80, 200)
    sales_units = int(base_sales - (inflation_rate * 2))

    data.append([
        date.strftime('%Y-%m-%d'),
        model,
        city,
        max(sales_units, 5),  # avoid negative sales
        inflation_rate
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'Date', 'Model', 'City', 'Sales_Units', 'Inflation_Rate'
])

# Save CSV
df.to_csv('suzuki_sales_data.csv', index=False)

print("✅ suzuki_sales_data.csv created successfully!")