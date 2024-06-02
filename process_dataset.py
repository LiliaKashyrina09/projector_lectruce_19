import pandas as pd

# Task 2a: Import the dataset
file_path = 'pandas_dataset.csv'
df = pd.read_csv(file_path)

# Task 2b: Select only the Team, Yellow Cards, and Red Cards columns
selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print("Selected Columns:")
print(selected_columns[['Team', 'Yellow Cards', 'Red Cards']])

# Task 2c: Count how many teams participated in the Euro 2012
number_of_teams = df['Team'].nunique()
print("\nNumber of teams participated in Euro 2012:", number_of_teams)

# Task 2d: Filter teams that scored more than 6 goals
teams_more_than_6_goals = df[df['Goals'] > 6]  
print("\nTeams that scored more than 6 goals:")
print(teams_more_than_6_goals[['Team', 'Goals']])
