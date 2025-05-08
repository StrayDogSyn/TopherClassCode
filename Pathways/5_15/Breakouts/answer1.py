# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Use the same mock temperature data provided to students
monthly_temps = {
    'Jan': [1.3, -2.5, 0.2, -1.5, 2.3, 0.8, -3.2, -2.5, 1.2, -0.8, 
            -1.5, 2.1, 0.5, -2.8, -0.4, -1.9, 0.7, -3.5, -2.2, 0.9, 
            -1.1, -0.3, 1.8, -2.1, 0.3, 1.1, -1.7, -0.9, -15.0, 0.4],
    
    'Feb': [0.2, 2.5, -1.3, 3.8, 1.7, -2.1, 4.2, 0.8, -3.5, 2.9, 
            -0.7, 5.1, 1.3, -2.8, 3.3, 0.5, -1.9, 4.7, 2.1, -0.3, 
            5.5, 3.2, 0.1, -2.4, 4.3, 1.5, -3.1, 3.7, 0.3, 2.8],
    
    'Mar': [4.8, 7.2, 5.5, 3.1, 8.4, 6.7, 9.3, 5.2, 4.0, 7.9, 
            6.3, 8.8, 5.7, 3.5, 9.1, 7.5, 4.3, 6.8, 8.2, 5.9, 
            3.8, 7.3, 9.5, 6.1, 4.9, 8.0, 5.3, 7.7, 4.5, 6.5],
    
    'Apr': [12.3, 9.8, 11.5, 14.2, 10.7, 13.0, 9.5, 12.8, 15.0, 11.2, 
            14.5, 10.3, 13.7, 11.9, 9.2, 14.8, 12.1, 10.5, 13.3, 15.2, 
            11.7, 14.0, 10.1, 12.5, 15.5, 13.8, 10.9, 14.3, 11.3, 12.7],
    
    'May': [16.5, 18.2, 17.0, 19.8, 16.7, 18.5, 17.3, 19.0, 16.2, 18.8, 
            17.5, 19.3, 16.9, 18.0, 17.7, 19.5, 16.3, 18.7, 17.2, 19.2, 
            16.8, 18.3, 17.8, 19.7, 16.1, 18.9, 17.4, 19.1, 16.6, 18.1],
    
    'Jun': [21.3, 23.7, 20.5, 24.2, 22.8, 26.0, 21.5, 25.3, 22.0, 24.8, 
            23.2, 20.7, 25.5, 21.7, 24.5, 23.0, 26.3, 22.5, 20.2, 25.8, 
            23.5, 21.0, 24.0, 22.3, 25.0, 23.8, 21.8, 24.7, 22.7, 20.9],
    
    'Jul': [25.8, 28.3, 27.0, 30.5, 29.2, 26.5, 31.0, 27.5, 29.8, 28.7, 
            26.2, 30.0, 28.5, 27.2, 29.5, 31.2, 28.0, 26.8, 30.7, 29.0, 
            27.8, 31.5, 29.3, 26.3, 28.8, 30.2, 27.3, 29.7, 38.0, 28.2],
    
    'Aug': [26.3, 29.8, 28.0, 24.5, 27.3, 30.2, 28.7, 25.5, 29.0, 27.7, 
            24.0, 28.3, 30.5, 27.0, 29.3, 26.5, 28.8, 25.0, 29.5, 27.5, 
            30.0, 26.0, 28.5, 24.8, 27.8, 29.2, 26.8, 30.7, 28.2, 25.8],
    
    'Sep': [22.0, 20.7, 23.5, 21.3, 24.0, 22.8, 21.5, 23.2, 20.5, 22.5, 
            23.8, 21.0, 22.3, 20.2, 23.0, 21.8, 24.2, 22.2, 20.8, 23.7, 
            21.7, 24.5, 22.7, 21.2, 23.3, 20.3, 22.8, 24.7, 21.5, 23.0],
    
    'Oct': [15.7, 13.2, 16.5, 12.8, 14.3, 17.0, 13.8, 15.2, 14.0, 16.3, 
            12.5, 15.0, 13.5, 16.8, 14.7, 12.2, 15.5, 17.2, 13.0, 14.8, 
            16.0, 12.7, 15.3, 14.5, 17.7, 13.3, 16.2, 12.0, 14.2, 15.8],
    
    'Nov': [7.2, 9.8, 6.5, 10.3, 8.7, 5.0, 9.5, 7.8, 11.0, 6.3, 
            8.2, 10.5, 7.0, 9.2, 5.8, 8.5, 6.8, 10.8, 9.0, 7.5, 
            5.5, 8.0, 10.0, 7.3, 9.7, 6.0, 8.8, 7.7, 5.3, 9.3],
    
    'Dec': [2.7, -0.5, 3.8, 1.0, -1.8, 2.3, 0.2, -2.5, 3.0, 1.5, 
            -1.0, 2.0, -3.2, 1.2, 3.5, 0.8, -2.2, 2.5, 0.5, -1.5, 
            3.2, 1.8, -0.3, 2.2, 0.0, -2.8, 15.0, 1.3, -1.3, 2.8]
}

# Convert the dictionary to a DataFrame
data = []
for month, temps in monthly_temps.items():
    for temp in temps:
        data.append({'month': month, 'temperature': temp})

temperatures = pd.DataFrame(data)

# Make sure months are in correct order (Jan to Dec)
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperatures['month'] = pd.Categorical(temperatures['month'], 
                                      categories=month_order, 
                                      ordered=True)

# Solution 1: Basic box plot with Matplotlib
plt.figure(figsize=(12, 6))
temperatures.boxplot(column='temperature', by='month', figsize=(12, 6))
plt.title('Monthly Temperature Distributions')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.suptitle('')  # Remove the automatic title
plt.tight_layout()
plt.show()

# Solution 2: Enhanced box plot with Seaborn
plt.figure(figsize=(12, 6))
sns.boxplot(x='month', y='temperature', data=temperatures, 
            palette="coolwarm")  # Use a color palette to show temperature differences

plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Distributions')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('plot.png')