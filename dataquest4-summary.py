#%% [markdown]
# # Exploratory Data Visualization
# ## Line Chart

#%%
# Importing the pyplot module
import matplotlib.pyplot as plt

#%%
# Generating and displaying the plot
plt.plot()
plt.show()

#%%
# Generating a line chart
plt.plot(first_twelve["DATE"], first_twelve["VALUE"])

#%%
# To rotate axis ticks
plt.xticks(rotation=90)

#%%
# To add axis label
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")

#%%
plt.title("Monthly Unemployment Trends, 1948")