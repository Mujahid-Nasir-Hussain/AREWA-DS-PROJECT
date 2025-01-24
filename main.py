import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Generate Random Data
np.random.seed(42)
categories = ['Group A', 'Group B', 'Group C']
data = pd.DataFrame({
    'Category': np.random.choice(categories, 200),
    'Value': np.random.normal(loc=50, scale=10, size=200)
})

# Visualize Data
# Histogram
plt.hist(data['Value'], bins=20, color='skyblue', alpha=0.7)
plt.title('Histogram of Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Boxplot
sns.boxplot(x='Category', y='Value', data=data)
plt.title('Boxplot of Values by Category')
plt.show()

# Scatter Plot (Interactive)
fig = px.scatter(data, x=data.index, y='Value', color='Category', title='Scatter Plot of Values')
fig.show()
