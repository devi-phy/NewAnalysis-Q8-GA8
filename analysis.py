
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
retention_rates = [65.02, 71.48, 72.37, 75.86]
average_retention = np.mean(retention_rates)
industry_target = 85

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting the quarterly data
bars = ax.bar(quarters, retention_rates, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'], label='Quarterly Retention Rate')

# Adding the industry target line
ax.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target}%)')

# Adding the average retention line
ax.axhline(y=average_retention, color='b', linestyle=':', label=f'Average Retention ({average_retention:.2f}%)')

# Adding labels and title
ax.set_ylim(0, 100)
ax.set_ylabel('Customer Retention Rate (%)')
ax.set_xlabel('2024 Quarters')
ax.set_title('Quarterly Customer Retention Rate vs. Industry Target')
ax.legend()

# Adding data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}%', va='bottom', ha='center')

# Save the chart to a file
plt.savefig('retention_chart.png')

print("Chart saved as retention_chart.png")
