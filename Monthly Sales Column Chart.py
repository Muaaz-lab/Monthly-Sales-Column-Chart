import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [120, 150, 180, 160, 200, 240]

plt.figure(figsize=(9,5))

bars = plt.bar(months, sales, width=0.6)

# Labels & Title
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Column Chart")

# Add grid (only for y-axis)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3, str(height),
             ha='center', va='bottom', fontsize=10)

plt.show()
# version 2
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [120, 150, 180, 160, 200, 240]

colors = ['red', 'orange', 'blue', 'green', 'purple', 'brown']

plt.figure(figsize=(9,5))

bars = plt.bar(months, sales, color=colors, width=0.6)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Column Chart (Colored)")

plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3, str(height),
             ha='center', va='bottom', fontsize=10)

plt.show()
#version 3 of sales
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [120, 150, 180, 160, 200, 240]

# Find max value
max_sale = max(sales)

# Assign colors (highlight max month)
colors = ['orange' if s == max_sale else 'skyblue' for s in sales]

plt.figure(figsize=(9,5))
bars = plt.bar(months, sales, color=colors, width=0.6)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Column Chart (Highest Highlighted)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add values on top
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3, str(height),
             ha='center', va='bottom', fontsize=10)

plt.show()
# super optimization of Monthly revenue and sales
import matplotlib.pyplot as plt

# -------------------------
# Dataset 1: Revenue
months_rev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [45000, 42000, 48000, 51000, 53000, 59000, 62000, 61000, 58000, 64000, 89000, 115000]

# Highlight highest revenue
max_rev = max(revenue)
colors_rev = ['orange' if r == max_rev else 'skyblue' for r in revenue]

plt.figure(figsize=(12,5))
bars = plt.bar(months_rev, revenue, color=colors_rev, width=0.6)
plt.title("Monthly Revenue (USD) - Highest Highlighted")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3000, f"${height:,}", ha='center', va='bottom', fontsize=10)

plt.show()

# -------------------------
# Dataset 2: Visitors
months_vis = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
visitors = ["1,200","1,350","1,600","1,850","2,100","2,450","2,800","3,100","3,400","3,900","4,500","5,200"]

# Convert visitors to int
visitors = [int(v.replace(",","")) for v in visitors]

# Highlight highest visitors
max_vis = max(visitors)
colors_vis = ['orange' if v == max_vis else 'skyblue' for v in visitors]

plt.figure(figsize=(12,5))
bars = plt.bar(months_vis, visitors, color=colors_vis, width=0.6)
plt.title("Monthly Visitors - Highest Highlighted")
plt.xlabel("Month")
plt.ylabel("Number of Visitors")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 50, f"{height:,}", ha='center', va='bottom', fontsize=10)

plt.show()
