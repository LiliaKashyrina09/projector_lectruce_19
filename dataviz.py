import seaborn as sns
import matplotlib.pyplot as plt

#Plot Type: Scatter Plot
#Use Case: relationship between two variables
tips = sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title(' Total Bill vs Tip')
plt.show()

#Plot Type: Line Plot
#Use Case: trends over time 
flights = sns.load_dataset('flights')
flights_summary = flights.pivot_table(index='year', columns='month', values='passengers', aggfunc='sum')
sns.lineplot(data=flights_summary.sum(axis=1))
plt.title('Total Passengers Per Year')
plt.ylabel('Total Passengers')
plt.show()

#Plot Type: Histogram
#Use Case: visualize the distribution of a variable
diamonds = sns.load_dataset('diamonds')
sns.histplot(data=diamonds, x='price', bins=30, kde=True)
plt.title('Distribution of Diamond Prices')
plt.show()

#Plot Type: Box Plot
#Use Case: distribution of a dataset and spotting outliers
tips = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Box Plot of Total Bills by Day')
plt.show()




