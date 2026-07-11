import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
data = pd.read_csv("dataset/sales.csv")


# Convert Date column
data["Date"] = pd.to_datetime(data["Date"])


print("Sales Data Analysis Dashboard")

# Total sales

total_sales = data["Sales"].sum()
print("Total Sales:", total_sales)


# Best selling product

best_product = data.groupby("Product")["Sales"].sum().idxmax()
print("Best Selling Product:", best_product)


# Sales category

category_sales = data.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)


# Plot category 

plt.figure(figsize=(7,5))

category_sales.plot(
    kind="bar",
    color=["blue", "green"]
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()


# Monthly sales

monthly_sales = data.groupby(
    data["Date"].dt.month
)["Sales"].sum()


plt.figure(figsize=(7,5))

monthly_sales.plot(
    marker="o",
    color="red"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()

plt.show()