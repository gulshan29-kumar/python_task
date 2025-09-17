import matplotlib.pyplot as plt

# Sales data (in thousands)
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

# Initialize variables
total_sales = 0
max_sales = sales_data[0]
max_month_index = 0

# Calculate total sales, find max sales and its month
for i in range(len(sales_data)):
    total_sales += sales_data[i]
    
    if sales_data[i] > max_sales:
        max_sales = sales_data[i]
        max_month_index = i

# Calculate average sales
average_sales = total_sales / len(sales_data)

print(f"Total Sales: {total_sales}k")
print(f"Average Monthly Sales: {average_sales:.2f}k")
print(f"Highest Sales Month: Month {max_month_index + 1} with {max_sales}k")

# Plotting the sales data
months = [f"Month {i+1}" for i in range(12)]

plt.figure(figsize=(12, 6))
bars = plt.bar(months, sales_data, color='skyblue')

# Highlight the month with highest sales
bars[max_month_index].set_color('orange')

plt.title("Monthly Sales Data (in Thousands)")
plt.xlabel("Month")
plt.ylabel("Sales (in thousands)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate the highest sales bar
plt.text(max_month_index, max_sales + 1, f"Max: {max_sales}k", 
         ha='center', fontweight='bold', color='red')

plt.tight_layout()
plt.show()