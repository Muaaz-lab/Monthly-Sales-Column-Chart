<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monthly Sales & Revenue Visualization with Python</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f7fa;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            text-align: center;
            margin-bottom: 40px;
        }
        h2 {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
        }
        p {
            font-size: 16px;
            line-height: 1.6;
        }
        pre {
            background-color: #ecf0f1;
            padding: 15px;
            border-left: 5px solid #3498db;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', monospace;
            color: #e74c3c;
        }
        .section {
            margin-bottom: 50px;
        }
        .note {
            background-color: #f1c40f;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Monthly Sales & Revenue Visualization with Python</h1>

    <div class="section">
        <h2>1. Simple Monthly Sales Column Chart</h2>
        <p>This chart visualizes monthly sales using a basic bar chart in Python's <code>matplotlib</code>. Each bar represents sales for a month.</p>
        <pre><code>import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [120, 150, 180, 160, 200, 240]

plt.figure(figsize=(9,5))
bars = plt.bar(months, sales, width=0.6)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Column Chart")
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3, str(height),
             ha='center', va='bottom', fontsize=10)

plt.show()</code></pre>
        <p class="note">Note: The <code>plt.text</code> function adds values on top of each bar for clarity.</p>
    </div>

    <div class="section">
        <h2>2. Colored Monthly Sales Chart</h2>
        <p>We can make the chart more attractive by assigning different colors to each bar.</p>
        <pre><code>colors = ['red', 'orange', 'blue', 'green', 'purple', 'brown']
bars = plt.bar(months, sales, color=colors, width=0.6)</code></pre>
        <p class="note">Each month now has a unique color to make it visually appealing.</p>
    </div>

    <div class="section">
        <h2>3. Highlighting the Highest Sales Month</h2>
        <p>We can highlight the month with the maximum sales to focus attention on peak performance.</p>
        <pre><code>max_sale = max(sales)
colors = ['orange' if s == max_sale else 'skyblue' for s in sales]
bars = plt.bar(months, sales, color=colors, width=0.6)</code></pre>
        <p class="note">The highest month is colored orange, while the rest are skyblue.</p>
    </div>

    <div class="section">
        <h2>4. Super Optimized Monthly Revenue and Visitors Charts</h2>
        <p>This section combines two datasets: <strong>Revenue</strong> and <strong>Visitors</strong>, with the highest value highlighted for each.</p>

        <h3>Revenue Dataset</h3>
        <pre><code>months_rev = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [45000, 42000, 48000, 51000, 53000, 59000, 62000, 61000, 58000, 64000, 89000, 115000]

max_rev = max(revenue)
colors_rev = ['orange' if r == max_rev else 'skyblue' for r in revenue]

plt.figure(figsize=(12,5))
bars = plt.bar(months_rev, revenue, color=colors_rev, width=0.6)
plt.title("Monthly Revenue (USD) - Highest Highlighted")
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3000, f"${height:,}", ha='center', va='bottom', fontsize=10)

plt.show()</code></pre>

        <h3>Visitors Dataset</h3>
        <pre><code>months_vis = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
visitors = ["1,200","1,350","1,600","1,850","2,100","2,450","2,800","3,100","3,400","3,900","4,500","5,200"]
visitors = [int(v.replace(",","")) for v in visitors]

max_vis = max(visitors)
colors_vis = ['orange' if v == max_vis else 'skyblue' for v in visitors]

plt.figure(figsize=(12,5))
bars = plt.bar(months_vis, visitors, color=colors_vis, width=0.6)
plt.title("Monthly Visitors - Highest Highlighted")
plt.xlabel("Month")
plt.ylabel("Number of Visitors")
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 50, f"{height:,}", ha='center', va='bottom', fontsize=10)

plt.show()</code></pre>
        <p class="note">Both charts use the same highlighting technique to emphasize the highest month.</p>
    </div>

    <div class="section">
        <h2>Key Concepts Covered</h2>
        <ul>
            <li>Creating bar charts with <code>matplotlib</code>.</li>
            <li>Customizing bar colors to make charts more visually attractive.</li>
            <li>Highlighting maximum values using conditional coloring.</li>
            <li>Adding value labels on top of bars for clarity.</li>
            <li>Using <code>grid</code> to improve readability of charts.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Conclusion</h2>
        <p>These techniques make your charts more informative and eye-catching. Using Python's <code>matplotlib</code>, you can visualize sales, revenue, and visitors easily while emphasizing key data points.</p>
    </div>

</body>
</html>
