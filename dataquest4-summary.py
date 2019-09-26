#%% [markdown]
# # Exploratory Data Visualization
# ## Line Chart

#%%
# Importing the pyplot module
import matplotlib.pyplot as plt

#%%
# Generating and displaying the plot
plt.plot() # plt.plot(x_values, y_values)
plt.show()

#%%
# Generating a line chart
import pandas as pd
unrate = pd.read_csv("unrate.csv")
unrate['DATE'] = pd.to_datetime(unrate["DATE"])
first_twelve = unrate[:12]
plt.plot(first_twelve["DATE"], first_twelve["VALUE"])
plt.xticks(rotation=90) # to rotate axis ticks
plt.xlabel("Month") # add x-axis label
plt.ylabel("Unemployment Rate") # add y-axis label
plt.title("Monthly Unemployment Trends, 1948") # add title
plt.show()

#%% [markdown]
# ## Multiple Plots

#%%
# Creating a figure using the pyplot module
fig = plt.figure()

# Adding a subplot to an existing figure with 2 plots and 1 column, one above the other
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.plot(unrate['DATE'][:12], unrate['VALUE'][:12])
ax2.plot(unrate['DATE'][12:24], unrate['VALUE'][12:24])
plt.show()

#%%[markdown]
# `axes_obj = fig.add_subplot(nrows, ncols, plot_number)`

#%%
# Changing the dimensions of the figure with the figsize parameter (width x height)
fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
# Generating a line chart within an Axes object
ax1.plot(unrate.iloc[0:12,0], unrate.iloc[0:12,1])
ax2.plot(unrate.iloc[12:24,0], unrate.iloc[12:24,1])

# Setting the title for Axes_1 object
ax1.set_title("Unemployment Trend, 1948")
ax2.set_title("Unemployment Trend, 1948")
plt.show()

#%%
# Using `for` loop for the subplot
fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset["DATE"], subset["VALUE"])
plt.show()

#%%
# Specifiying hte color for a certain line using the "c" parameter
unrate["MONTH"] = unrate["DATE"].dt.month
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]["VALUE"], c = "red")
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]["VALUE"], c = "blue")
plt.show()

#%%
fig = plt.figure(figsize=(10,6))
colors = ['red','blue','green','orange','black']

for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    label = str(1948+i)
    plt.plot(subset["MONTH"], subset["VALUE"], c = colors[i], label = label)
plt.legend(loc="upper left")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")
plt.title("Unemployment Trend, 1948")
plt.show()

#%%
# Setting the title for Axes object
ax.set_title("Unemployment Trend, 1948")

#%% [markdown]
# ## Bar Plots and Scatter Plots

#%%
# Importing data
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

reviews = pd.read_csv("fandango_scores.csv")
cols = ['FILM','RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']
norm_reviews = reviews[cols]

#%%
# Generating a vertical bar plot
num_cols = ['RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values # return the first row of the `num_cols`
bar_position = arange(5) + 0.75 # Using arange to return evenly seperated values
fig,ax = plt.subplots()
plt.bar(bar_position, bar_heights, 0.5)

#%%
# Generating a vertical bar plot
num_cols = ['RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_position = arange(5) + 0.75
tick_position = range(1,6)
fig,ax = plt.subplots()
ax.bar(bar_position, bar_heights, 0.5)
ax.set_xticks(tick_position) # set veritcal in a list of tick location
ax.set_xticklabels(num_cols, rotation = 90) # set vertica  in a list of labels with 90 degree of rotation
ax.set_xlabel("Rating Source")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

#%%
# Generating a horizontal bar plot
num_cols = ['RT_user_norm','Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_position = arange(5) + 0.75
tick_position = range(1,6)
fig,ax = plt.subplots()
ax.bar(bar_position, bar_heights, 0.5)
ax.set_xticks(tick_position) # set horizontal in a list of tick location
ax.set_yticklabels(num_cols) # set horizontal in a list of labels 
ax.set_xlabel("Rating Source")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

#%%
# Using Axes.scatter() to create a scatter plot
fig,ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews["RT_user_norm"])
ax.set_xlabel("Fandango")
ax.set_ylabel("Rotten Tomatoes")
plt.show()

#%%
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["RT_user_norm"])
ax1.set_xlim(0,5)
ax1.set_ylim(0,5)
ax1.set_xlabel("Fandango")
ax1.set_ylabel("Rotten Tomatoes")

ax2.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["Metacritic_user_nom"])
ax2.set_xlim(0,5)
ax2.set_ylim(0,5)
ax2.set_xlabel("Fandango")
ax2.set_ylabel("Metacritic")

ax3.scatter(norm_reviews["Fandango_Ratingvalue"], norm_reviews["IMDB_norm"])
ax3.set_xlim(0,5)
ax3.set_ylim(0,5)
ax3.set_xlabel("Fandango")
ax3.set_ylabel("IMDB")

plt.show()

#%% [markdown]
# ## Histogram and Box Plots

#%%
# Creating a frequency distribution
fandango_dist = norm_reviews['Fandango_Ratingvalue'].value_counts().sort_index()

imdb_dist = norm_reviews['IMDB_norm'].value_counts().sort_index()

#%%
# Creating a histogram
fig,ax = plt.subplots()
ax.hist(norm_reviews['Fandango_Ratingvalue'], range = (0,5))
plt.show()

#%%
fig = plt.figure(figsize=(5,20))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.hist(norm_reviews["Fandango_Ratingvalue"], bins = 20, range = (0,5))
ax1.set_title("Distribution of Fandango Ratings")
ax1.set_ylim(0, 50)

ax2.hist(norm_reviews["RT_user_norm"], bins = 20, range = (0,5))
ax2.set_title("Distribution of Rotten Tomatoes Ratings")
ax2.set_ylim(0, 50)

ax3.hist(norm_reviews["Metacritic_user_nom"], bins = 20, range = (0,5))
ax3.set_title("Distribution of Metacritic Ratings")
ax3.set_ylim(0, 50)

ax4.hist(norm_reviews["IMDB_norm"], bins = 20, range = (0,5))
ax4.set_title("Distribution of IMDB Ratings")
ax4.set_ylim(0, 50)

plt.show()

#%%
# Creating a boxplot
import seaborn as sns
fig, ax = plt.subplots()
sns.boxplot(y=norm_reviews['RT_user_norm'])
ax.set_ylim(0,5)
plt.xlabel("Rotten Tomatos")

#%%
import pandas as pd
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm = pd.melt(norm_reviews[num_cols])
bp = sns.boxplot(x="variable",y="value", data=norm)
bp.set_xticklabels(bp.get_xticklabels(),rotation=90)
plt.show()